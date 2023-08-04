from django.urls import path
from .views import BalanceDetailAPIView

app_name = 'balance'

urlpatterns = [
    path('balance/<int:pk>/', BalanceDetailAPIView.as_view(), name='balance-detail'),
]
