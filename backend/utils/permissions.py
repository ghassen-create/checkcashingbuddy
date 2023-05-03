from django.conf import settings
from rest_framework.permissions import BasePermission


class ViewAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user and settings.ADMIN_GROUP_NAME in [obj.name for obj in request.user.groups.all()]:
            return True

        return False


class ViewStore(BasePermission):
    def has_permission(self, request, view):
        if request.user and settings.STORE_GROUP_NAME in [obj.name for obj in request.user.groups.all()]:
            return True

        return False


class ViewCustomer(BasePermission):
    def has_permission(self, request, view):
        if request.user and settings.CUSTOMER_GROUP_NAME in [obj.name for obj in request.user.groups.all()]:
            return True

        return False
