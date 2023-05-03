from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from utils.permissions import ViewAdmin, ViewStore

from .filters import ReportFilter
from report.models import Report
from .serializers import ReportSerializer
from utils.views import filter_user_restrictions


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.order_by('-id')
    serializer_class = ReportSerializer
    permission_classes = [ViewAdmin | ViewStore]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ReportFilter

    def get_queryset(self):
        queryset = filter_user_restrictions(super().get_queryset(), self.request.user)
        return queryset

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        net_total = sum([r.amount - ((r.commission * r.amount) / 100) for r in self.get_queryset()])
        total_amount = self.get_queryset().aggregate(Sum('amount'))['amount__sum']
        response.data['total_amount'] = total_amount
        response.data['net_total'] = net_total
        return response
