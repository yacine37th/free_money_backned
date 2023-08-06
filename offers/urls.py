from django.urls import path
from .views import OfferListAPIView, OfferDetailAPIView

app_name = 'offers'

urlpatterns = [
    path('offers/', OfferListAPIView.as_view(), name='offer-list'),
    path('offers/<int:pk>/', OfferDetailAPIView.as_view(), name='offer-detail'),
]
