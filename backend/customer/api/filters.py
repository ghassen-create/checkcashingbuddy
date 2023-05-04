import django_filters

from customer.models import CustomerAvatar, CustomerNote, CustomerDriverLicence, Customer


class CustomerFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")
    address_1 = django_filters.CharFilter(field_name="address_1", lookup_expr="icontains")
    birth_date = django_filters.DateFilter(field_name="birth_date")

    class Meta:
        model = Customer
        fields = "__all__"


class AvatarFilter(django_filters.FilterSet):
    customer_id = django_filters.NumberFilter(field_name="customer_id")

    class Meta:
        model = CustomerAvatar
        fields = ["customer_id"]


class NoteFilter(django_filters.FilterSet):
    customer_id = django_filters.NumberFilter(field_name="customer_id")

    class Meta:
        model = CustomerNote
        fields = ["customer_id"]


class DriverLicenceFilter(django_filters.FilterSet):
    customer_id = django_filters.NumberFilter(field_name='customer_id')

    class Meta:
        model = CustomerDriverLicence
        fields = ["customer_id"]
