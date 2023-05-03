from django.contrib import admin

from .models import Avatar, Note, DriverLicence

# Register your models here.
admin.site.register(Avatar)
admin.site.register(Note)
admin.site.register(DriverLicence)
