from rest_framework import serializers
from .models import CashoutRequest

class CashoutRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashoutRequest
        fields = ('id', 'user', 'requested_points', 'payment_method','payment_address', 'status')
