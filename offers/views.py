from rest_framework import generics
from .models import Offer
from .serializers import OfferSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import OfferLog
from .serializers import OfferLogSerializer, OfferLogCreateSerializer


class OfferListAPIView(generics.ListAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

class OfferDetailAPIView(generics.RetrieveAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer



class OfferLogListView(generics.ListCreateAPIView):
    queryset = OfferLog.objects.all()
    serializer_class = OfferLogSerializer

    def perform_create(self, serializer):
        user_id = self.request.data.get('user_id')  # Assuming you're sending 'user_id' from the frontend
        serializer.save(user=user_id)


class OfferLogCreateView(generics.CreateAPIView):
    queryset = OfferLog.objects.all()
    serializer_class = OfferLogCreateSerializer