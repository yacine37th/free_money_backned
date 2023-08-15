from rest_framework import generics
from .models import Balance
from .serializers import BalanceSerializer, UpdateBalanceSerializer
from rest_framework.response import Response

class BalanceDetailAPIView(generics.RetrieveAPIView):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer


class UpdateBalanceAPIView(generics.UpdateAPIView):
    queryset = Balance.objects.all()
    serializer_class = UpdateBalanceSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
