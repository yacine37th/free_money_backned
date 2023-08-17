from django.urls import path
from .views import OfferListAPIView, OfferDetailAPIView, OfferLogListView, OfferLogCreateView

app_name = 'offers'

urlpatterns = [
    path('offers/', OfferListAPIView.as_view(), name='offer-list'),
    path('offers/<int:pk>/', OfferDetailAPIView.as_view(), name='offer-detail'),
    path('offer-logs/', OfferLogListView.as_view(), name='offer-log-list'),
    path('post-offer-logs/', OfferLogCreateView.as_view(), name='offer-log-list'),
    ]
