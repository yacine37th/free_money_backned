
from django.contrib import admin
from django.urls import include, path

# urls
urlpatterns = [
    path('api/v1/movies/', include('movies.urls')),
    path('api/v1/auth/', include('authentication.urls')),
    path('api/v1/', include('offers.urls')),
    path('api/v1/', include('checkout.urls')),
    path('api/v1/', include('balance.urls')),
    path('api/v1/', include('cards.urls')),
    path('admin/', admin.site.urls),
]