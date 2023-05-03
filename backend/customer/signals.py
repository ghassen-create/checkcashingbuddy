from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Avatar, Note, DriverLicence, Customer
from store.models import StoreCustomer


@receiver(post_save, sender=Customer)
def update_avatar_current(sender, instance, created, **kwargs):
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
        if user.store_id:
            StoreCustomer.objects.create(
                store_id=user.store_id,
                customer=instance
            )


@receiver(post_save, sender=Avatar)
def update_avatar_current(sender, instance, created, **kwargs):
    if created:
        avatars = Avatar.objects.filter(customer=instance.customer)
        for avatar in avatars:
            avatar.current = False
            avatar.save()
        instance.current = True
        instance.save()


@receiver(post_save, sender=Note)
def update_last_note(sender, instance, created, **kwargs):
    if created:
        notes = Note.objects.filter(customer=instance.customer)
        for note in notes:
            note.last = False
            note.save()
        instance.last = True
        instance.save()


@receiver(post_save, sender=DriverLicence)
def update_last_dl(sender, instance, created, **kwargs):
    if created:
        dls = DriverLicence.objects.filter(customer=instance.customer)
        for dl in dls:
            dl.current = False
            dl.save()
        instance.current = True
        instance.save()
