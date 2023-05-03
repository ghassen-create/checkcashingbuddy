from auditlog.models import LogEntry
from rest_framework import serializers

from check.models import Check


class CheckSerializer(serializers.ModelSerializer):
    customer_name = serializers.SerializerMethodField()
    store_name = serializers.SerializerMethodField()
    net_payment = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Check
        fields = "__all__"

    @staticmethod
    def get_net_payment(obj):
        return obj.net_payment

    @staticmethod
    def get_customer_name(obj):
        return obj.customer_name

    @staticmethod
    def get_store_name(obj):
        return obj.store_name

    @staticmethod
    def get_created_at(obj):
        return obj.get_created_at

    @staticmethod
    def get_updated_at(obj):
        return obj.get_updated_at


class CheckHistorySerializer(serializers.ModelSerializer):
    actor_username = serializers.SerializerMethodField()
    actor_fullname = serializers.SerializerMethodField()
    action_display = serializers.SerializerMethodField()
    timestamp = serializers.SerializerMethodField()

    class Meta:
        model = LogEntry
        fields = "__all__"

    @staticmethod
    def get_actor_username(obj):
        return obj.actor.username if obj.actor else ""

    @staticmethod
    def get_actor_fullname(obj):
        return obj.actor.get_full_name if obj.actor else ""

    @staticmethod
    def get_action_display(obj):
        return obj.get_action_display()

    @staticmethod
    def get_timestamp(obj):
        return (
            f"{obj.timestamp.date()} {obj.timestamp.strftime('%H:%M:%S')}"
            if obj.timestamp
            else ""
        )
