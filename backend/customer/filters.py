import django_filters

from .models import Avatar, Note, DriverLicence, Customer


class CustomerFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Customer
        fields = ["name"]


class AvatarFilter(django_filters.FilterSet):
    customer_id = django_filters.NumberFilter(field_name='customer_id')

    class Meta:
        model = Avatar
        fields = ["customer_id"]


class NoteFilter(django_filters.FilterSet):
    customer_id = django_filters.NumberFilter(field_name='customer_id')

    class Meta:
        model = Note
        fields = ["customer_id"]


class DLFilter(django_filters.FilterSet):
    customer_id = django_filters.NumberFilter(field_name='customer_id')

    class Meta:
        model = DriverLicence
        fields = ["customer_id"]