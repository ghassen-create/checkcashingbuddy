from django.contrib import admin

from .models import CustomerAvatar, CustomerNote, CustomerDriverLicence

# Register your models here.
admin.site.register(CustomerAvatar)
admin.site.register(CustomerNote)
admin.site.register(CustomerDriverLicence)
