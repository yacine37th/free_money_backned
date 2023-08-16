from rest_framework import serializers
from .models import CashoutRequest, CashOutLog

class CashoutRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashoutRequest
        fields = ('id', 'user', 'requested_points', 'payment_method','payment_address', 'status')


class CashOutLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashOutLog
        fields = ('id', 'user', 'cashout_request', 'payment_amount', 'payment_date')