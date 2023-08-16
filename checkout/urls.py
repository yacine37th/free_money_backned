from django.urls import path
from .views import CashoutRequestListAPIView, CashoutRequestDetailAPIView, CashOutLogListAPIView, CashOutLogDetailAPIView

app_name = 'cashout'

urlpatterns = [
    path('cashouts/', CashoutRequestListAPIView.as_view(), name='cashout-list'),
    path('cashouts/<int:pk>/', CashoutRequestDetailAPIView.as_view(), name='cashout-detail'),
    path('cashoutlogs/', CashOutLogListAPIView.as_view(), name='cashoutlog-list'),
    path('cashoutlogs/<int:pk>/', CashOutLogDetailAPIView.as_view(), name='cashoutlog-detail'),

]
