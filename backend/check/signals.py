from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Check
from report.models import Report


@receiver(post_save, sender=Check)
def create_report_instance(sender, instance, created, **kwargs):
    import inspect
    user = None
    try:
        for frame_record in inspect.stack():
            if frame_record[3] == 'get_response':
                request = frame_record[0].f_locals['request']
                user = request.user if request.user.is_authenticated else None
                break
    except Exception as e:
        pass
    if created:
        if user.store and settings.STORE_GROUP_NAME in [obj.name for obj in user.groups.all()]:
            instance.commission = user.store.commission if user.store.commission else 6
            instance.scanned_by_store = True
            instance.save()
        elif settings.ADMIN_GROUP_NAME in [obj.name for obj in user.groups.all()]:
            instance.commission = instance.commission if instance.commission else 6
            instance.scanned_by_admin = True
            instance.save()
        Report.objects.create(
            cheque=instance,
            amount=instance.amount,
            commission=instance.commission
        )
