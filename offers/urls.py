from django.urls import path
from .views import OfferListAPIView, OfferDetailAPIView, CompleteOfferView

app_name = 'offers'

urlpatterns = [
    path('offers/', OfferListAPIView.as_view(), name='offer-list'),
    path('offers/<int:pk>/', OfferDetailAPIView.as_view(), name='offer-detail'),
    path('offers/<int:offer_id>/complete/', CompleteOfferView.as_view(), name='complete-offer'),
]
