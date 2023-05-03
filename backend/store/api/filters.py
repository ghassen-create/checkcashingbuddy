import django_filters

from store.models import Store


class StoreFilter(django_filters.FilterSet):
    created_at = django_filters.DateRangeFilter(field_name="created_at")
    updated_at = django_filters.DateRangeFilter(field_name="updated_at")

    class Meta:
        model = Store
        fields = "__all__"
