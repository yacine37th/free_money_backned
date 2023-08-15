from django.urls import path
from .views import BalanceDetailAPIView, UpdateBalanceAPIView

app_name = 'balance'

urlpatterns = [
    path('balance/<int:pk>/', BalanceDetailAPIView.as_view(), name='balance-detail'),
    path('balance/<int:pk>/update/', UpdateBalanceAPIView.as_view(), name='balance-update'),

]
