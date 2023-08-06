from rest_framework import generics
from .models import Balance
from .serializers import BalanceSerializer

class BalanceDetailAPIView(generics.RetrieveAPIView):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer
