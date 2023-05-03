from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from store.models import Store, StoreCustomer

from .filters import StoreFilter
from .serializers import StoreSerializer, StoreCustomerSerializer
from utils.permissions import ViewAdmin, ViewStore

from utils.views import filter_user_restrictions


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.order_by("-id")
    serializer_class = StoreSerializer
    permission_classes = [ViewAdmin]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = StoreFilter

    def get_queryset(self):
        queryset = filter_user_restrictions(super().get_queryset(), self.request.user)
        return queryset


class StoreCustomerViewSet(viewsets.ModelViewSet):
    queryset = StoreCustomer.objects.order_by("-id")
    serializer_class = StoreCustomerSerializer
    permission_classes = [ViewAdmin | ViewStore]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    def get_queryset(self):
        queryset = filter_user_restrictions(super().get_queryset(), self.request.user)
        return queryset
