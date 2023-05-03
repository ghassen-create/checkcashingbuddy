from django.contrib import admin
from django.contrib.admin.models import LogEntry

from .models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ("username", "first_name", "last_name", "avatar", "groups", "user_permissions")
    filter_horizontal = ["groups", "user_permissions"]
    search_fields = ['username',
                     'first_name',
                     'last_name',
                     'is_superuser',
                     'is_staff',
                     'is_active']
    list_display = ['username', "first_name", "last_name", 'is_superuser', 'is_staff', 'is_active']
    list_filter = ['is_superuser', 'is_staff', 'is_active']
    readonly_fields = ('date_joined', 'updated_at', 'last_login')
