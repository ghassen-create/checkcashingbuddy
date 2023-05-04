from rest_framework import serializers

from customer.models import CustomerAvatar, CustomerNote, CustomerDriverLicence, Customer


class CustomerSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = "__all__"

    @staticmethod
    def get_created_at(obj):
        return obj.get_created_at

    @staticmethod
    def get_updated_at(obj):
        return obj.get_updated_at


class AvatarSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    customer_name = serializers.SerializerMethodField()

    class Meta:
        model = CustomerAvatar
        fields = "__all__"

    @staticmethod
    def get_created_at(obj):
        return obj.get_created_at

    @staticmethod
    def get_updated_at(obj):
        return obj.get_updated_at

    @staticmethod
    def get_customer_name(obj):
        return obj.customer_name


class NoteSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    customer_name = serializers.SerializerMethodField()

    class Meta:
        model = CustomerNote
        fields = "__all__"

    @staticmethod
    def get_created_at(obj):
        return obj.get_created_at

    @staticmethod
    def get_updated_at(obj):
        return obj.get_updated_at

    @staticmethod
    def get_customer_name(obj):
        return obj.customer_name


class DriverLicenceSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    customer_name = serializers.SerializerMethodField()

    class Meta:
        model = CustomerDriverLicence
        fields = "__all__"

    @staticmethod
    def get_created_at(obj):
        return obj.get_created_at

    @staticmethod
    def get_updated_at(obj):
        return obj.get_updated_at

    @staticmethod
    def get_customer_name(obj):
        return obj.customer_name
