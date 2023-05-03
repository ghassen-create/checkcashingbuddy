from accounts.models import User
from django.contrib.auth.models import Group, Permission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny
from utils.permissions import ViewAdmin

from .filters import GroupFilter, PermissionFilter, UserFilter
from .serializers import RegistrationSerializer, GroupSerializer, PermissionSerializer, UserSerializer


class RegistrationViewSet(viewsets.ModelViewSet):
    serializer_class = RegistrationSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [ViewAdmin]
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = UserFilter


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.order_by("-id")
    permission_classes = [ViewAdmin]
    serializer_class = GroupSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = GroupFilter


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.order_by("-id")
    permission_classes = [ViewAdmin]
    serializer_class = PermissionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = PermissionFilter
