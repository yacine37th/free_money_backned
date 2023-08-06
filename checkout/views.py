from rest_framework import generics
from .models import CashoutRequest
from .serializers import CashoutRequestSerializer

class CashoutRequestListAPIView(generics.ListCreateAPIView):
    queryset = CashoutRequest.objects.all()
    serializer_class = CashoutRequestSerializer

class CashoutRequestDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = CashoutRequest.objects.all()
    serializer_class = CashoutRequestSerializer
