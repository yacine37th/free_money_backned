from rest_framework import generics
from .models import Offer
from .serializers import OfferSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CompletedOffer


class OfferListAPIView(generics.ListAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

class OfferDetailAPIView(generics.RetrieveAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class CompleteOfferView(APIView):
    def post(self, request, offer_id):
        offer = Offer.objects.get(pk=offer_id)
        user = request.user

        # Check if the user has already completed this offer
        if CompletedOffer.objects.filter(user=user, offer=offer).exists():
            return Response({"message": "You have already completed this offer."}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new CompletedOffer instance
        completed_offer = CompletedOffer(user=user, offer=offer)
        completed_offer.save()

        return Response({"message": "Offer completed successfully."}, status=status.HTTP_201_CREATED)