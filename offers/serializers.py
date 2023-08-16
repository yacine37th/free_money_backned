from rest_framework import serializers
from .models import Offer, OfferLog

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('id', 'name', 'description', 'image_url','payout_amount', 'url')

class OfferLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferLog
        fields = ('user', 'offer', 'offer_amount', 'log_date')