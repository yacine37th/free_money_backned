from rest_framework import serializers
from .models import Offer, CompletedOffer

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('id', 'name', 'description', 'image_url','payout_amount', 'url')

class CompletedOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletedOffer
        fields = ('user', 'offer', 'completed_at')