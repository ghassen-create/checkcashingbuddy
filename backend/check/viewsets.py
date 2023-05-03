from auditlog.models import LogEntry
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from .filters import CheckFilter, CheckHistoryFilter
from .models import Check
from utils.permissions import ViewAdmin, ViewStore

from .serializers import CheckSerializer, CheckHistorySerializer
from utils.views import filter_user_restrictions


class CheckViewSet(viewsets.ModelViewSet):
    queryset = Check.objects.order_by("-id")
    permission_classes = [ViewAdmin | ViewStore]
    serializer_class = CheckSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = CheckFilter

    def get_queryset(self):
        queryset = filter_user_restrictions(super().get_queryset(), self.request.user)
        return queryset


class CheckHistoryViewSet(viewsets.ModelViewSet):
    queryset = LogEntry.objects.all()
    serializer_class = CheckHistorySerializer
    permission_classes = [ViewAdmin]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = CheckHistoryFilter
