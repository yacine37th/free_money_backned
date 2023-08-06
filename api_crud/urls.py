
from django.contrib import admin
from django.urls import include, path
from django.conf import settings # new
from django.conf.urls.static import static #new

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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)
