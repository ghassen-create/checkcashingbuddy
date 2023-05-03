import django_filters

from check.models import Check


class CheckFilter(django_filters.FilterSet):
    amount = django_filters.CharFilter(field_name="amount", lookup_expr="icontains")
    commission = django_filters.CharFilter(field_name="commission", lookup_expr="icontains")
    customer_id = django_filters.NumberFilter(field_name='customer_id')
    store_id = django_filters.NumberFilter(field_name='store_id')
    created_at = django_filters.DateRangeFilter(field_name="created_at")

    class Meta:
        model = Check
        fields = ["amount", "commission", "customer_id", "store_id", "created_at"]


class CheckHistoryFilter(django_filters.FilterSet):
    pass
