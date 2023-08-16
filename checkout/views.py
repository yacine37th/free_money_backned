from rest_framework import generics
from .models import CashoutRequest, CashOutLog
from .serializers import CashoutRequestSerializer, CashOutLogSerializer

class CashoutRequestListAPIView(generics.ListCreateAPIView):
    queryset = CashoutRequest.objects.all()
    serializer_class = CashoutRequestSerializer

class CashoutRequestDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = CashoutRequest.objects.all()
    serializer_class = CashoutRequestSerializer


class CashOutLogListAPIView(generics.ListCreateAPIView):
    queryset = CashOutLog.objects.all()
    serializer_class = CashOutLogSerializer

class CashOutLogDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = CashOutLog.objects.all()
    serializer_class = CashOutLogSerializer