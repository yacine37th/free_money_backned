from django.urls import path
from authentication.views import RegisterView, UserListView, UserDetailsView, CustomAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('token/', CustomAuthToken.as_view(), name='custom_token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserDetailsView.as_view(), name='user_details'),
]