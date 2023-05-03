from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from .filters import AvatarFilter, NoteFilter, DLFilter, CustomerFilter
from .models import Avatar, DriverLicence, Note, Customer
from utils.permissions import ViewAdmin, ViewStore

from .serializers import (
    AvatarSerializer,
    NoteSerializer,
    DriverLicenceSerializer,
    CustomerSerializer,
)
from utils.views import filter_user_restrictions


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.order_by("-id")
    permission_classes = [ViewAdmin | ViewStore]
    serializer_class = CustomerSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = CustomerFilter

    def get_queryset(self):
        queryset = filter_user_restrictions(super().get_queryset(), self.request.user)
        return queryset


class AvatarViewSet(viewsets.ModelViewSet):
    queryset = Avatar.objects.order_by("-id")
    permission_classes = [ViewAdmin | ViewStore]
    serializer_class = AvatarSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = AvatarFilter

    def get_queryset(self):
        queryset = filter_user_restrictions(super().get_queryset(), self.request.user)
        return queryset


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.order_by("-id")
    permission_classes = [ViewAdmin | ViewStore]
    serializer_class = NoteSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = NoteFilter

    def get_queryset(self):
        queryset = filter_user_restrictions(super().get_queryset(), self.request.user)
        return queryset


class DriverLicenceViewSet(viewsets.ModelViewSet):
    queryset = DriverLicence.objects.order_by("-id")
    permission_classes = [ViewAdmin | ViewStore]
    serializer_class = DriverLicenceSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = DLFilter

    def get_queryset(self):
        queryset = filter_user_restrictions(super().get_queryset(), self.request.user)
        return queryset
