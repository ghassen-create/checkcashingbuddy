from accounts.models import User
from django.contrib.auth.models import Group, Permission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from utils.permissions import ViewAdmin

from .filters import GroupFilter, PermissionFilter, UserFilter
from .serializers import RegistrationSerializer, GroupSerializer, PermissionSerializer, UserSerializer, LoginSerializer


class LoginAPIView(ObtainAuthToken):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        user_data = UserSerializer(user).data
        return Response({'token': token.key, 'user': user_data})


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
