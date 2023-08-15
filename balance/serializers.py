from rest_framework import serializers
from .models import Balance

class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = ('id', 'user', 'points')

class UpdateBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = ('points',)