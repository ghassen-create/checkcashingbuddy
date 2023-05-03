from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Avatar, Note, DriverLicence


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
