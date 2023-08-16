from rest_framework import generics
from .models import Offer
from .serializers import OfferSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import OfferLog
from .serializers import OfferLogSerializer


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
        serializer.save(user=self.request.user)