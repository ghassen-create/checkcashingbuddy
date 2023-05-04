from check.models import Check
from django.conf import settings
from django.db.models import Q

from report.models import Report

from customer.models import CustomerAvatar, CustomerDriverLicence, CustomerNote, Customer

from store.models import Store


# Create your views here.
def filter_user_restrictions(queryset, user):
    if queryset.model is Check:
        if user.store_id and settings.ADMIN_GROUP_NAME not in [obj.name for obj in user.groups.all()]:
            queryset = queryset.filter(
                Q(store_id=user.store_id)
            )
    if queryset.model is Customer:
        if user.store_id and settings.ADMIN_GROUP_NAME not in [obj.name for obj in user.groups.all()]:
            queryset = queryset.filter(
                Q(storecustomer__store_id=user.store_id)
            )
    if queryset.model is Store:
        if settings.ADMIN_GROUP_NAME not in [obj.name for obj in user.groups.all()]:
            queryset = queryset.filter(Q(user=user))
    if queryset.model is Report:
        if user.store_id and settings.ADMIN_GROUP_NAME not in [obj.name for obj in user.groups.all()]:
            queryset = queryset.filter(
                Q(cheque__store_id=user.store_id)
            )
    if queryset.model is StoreCustomer:
        if user.store_id and settings.ADMIN_GROUP_NAME not in [obj.name for obj in user.groups.all()]:
            queryset = queryset.filter(
                Q(store_id=user.store_id)
            )
    if queryset.model is CustomerAvatar or queryset.model is CustomerNote or queryset.model is CustomerDriverLicence:
        if user.store_id and settings.ADMIN_GROUP_NAME not in [obj.name for obj in user.groups.all()]:
            queryset = queryset.filter(
                Q(customer__storecustomer__store_id=user.store_id)
            )

    return queryset
