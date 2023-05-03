from rest_framework import serializers

from .models import Report


class ReportSerializer(serializers.ModelSerializer):
    net = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Report
        fields = "__all__"

    @staticmethod
    def get_net(obj):
        return obj.net_payment

    @staticmethod
    def get_created_at(obj):
        return obj.get_created_at
