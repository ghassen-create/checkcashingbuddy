import django_filters

from .models import Check


class CheckFilter(django_filters.FilterSet):
    amount = django_filters.CharFilter(field_name="amount", lookup_expr="icontains")
    commission = django_filters.CharFilter(field_name="commission", lookup_expr="icontains")
    customer_id = django_filters.NumberFilter(field_name='customer_id')

    class Meta:
        model = Check
        fields = ["amount", "commission", "customer_id"]


class CheckHistoryFilter(django_filters.FilterSet):
    pass
