from django.urls import path
from .views import CashoutRequestListAPIView, CashoutRequestDetailAPIView

app_name = 'cashout'

urlpatterns = [
    path('cashouts/', CashoutRequestListAPIView.as_view(), name='cashout-list'),
    path('cashouts/<int:pk>/', CashoutRequestDetailAPIView.as_view(), name='cashout-detail'),
]
