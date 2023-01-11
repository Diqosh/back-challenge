
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework.authtoken.views import obtain_auth_token

from challenge_function_based.views import registration_view

urlpatterns = [
    # Login and Register Token
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('register/', registration_view),

    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('admin/', admin.site.urls),
    path('challenge/', include('challenge.urls')),
    path('challenge_function_based/', include('challenge_function_based.urls')),
]
