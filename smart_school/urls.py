from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('school_api/', include('school_api.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
