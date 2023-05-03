from django.contrib.auth.models import update_last_login, Group, Permission
from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
)
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.state import token_backend

from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username", "password", "first_name", "last_name")

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["customer"] = UserSerializer(self.user).data
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.SerializerMethodField()
    last_login = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    groups_names = serializers.SerializerMethodField()
    store_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ["password"]
        read_only_field = ["is_active", "updated_at", "date_joined"]

    @staticmethod
    def get_groups_names(obj):
        return [group.name for group in obj.groups.all()]

    @staticmethod
    def get_date_joined(obj):
        return obj.get_date_joined

    @staticmethod
    def get_last_login(obj):
        return obj.get_last_login

    @staticmethod
    def get_updated_at(obj):
        return obj.get_updated_at

    @staticmethod
    def get_store_name(obj):
        return obj.store_name


class TokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super(TokenRefreshSerializer, self).validate(attrs)
        decoded_payload = token_backend.decode(data["access"], verify=True)
        user_uid = decoded_payload["user_id"]
        # add filter query

        obj = get_object_or_404(User, pk=user_uid)
        data["user"] = UserSerializer(obj).data
        groups = []
        perms = []
        for group in obj.groups.all():
            groups.append(group.name)
            for perm in group.permissions.all():
                perms.append(perm.codename)
            for perm in obj.user_permissions.all():
                perms.append(perm.codename)
        perms = tuple(perms)
        data.update({"groups_name": groups, "permissions_name": perms})
        return data


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"
