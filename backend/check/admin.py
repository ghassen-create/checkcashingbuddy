from django.contrib import admin

from .models import Check


# Register your models here.
@admin.register(Check)
class CheckAdmin(admin.ModelAdmin):
    list_display = ["customer_name", "amount"]
