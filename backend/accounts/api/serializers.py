from accounts.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group, Permission
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'groups')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label="Token",
        read_only=True
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.SerializerMethodField()
    last_login = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    groups_names = serializers.SerializerMethodField()
    store_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ["password"]
        read_only_field = ['is_active', 'updated_at', 'date_joined']

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


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"
