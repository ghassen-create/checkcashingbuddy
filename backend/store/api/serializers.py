from rest_framework import serializers

from store.models import Store, StoreCustomer


class StoreSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Store
        fields = "__all__"

    @staticmethod
    def get_created_at(obj):
        return obj.get_created_at

    @staticmethod
    def get_updated_at(obj):
        return obj.get_updated_at


class StoreCustomerSerializer(serializers.ModelSerializer):
    store_name = serializers.SerializerMethodField()
    customer_name = serializers.SerializerMethodField()

    class Meta:
        model = StoreCustomer
        fields = "__all__"

    @staticmethod
    def get_store_name(obj):
        return obj.store_name

    @staticmethod
    def get_customer_name(obj):
        return obj.customer_name
