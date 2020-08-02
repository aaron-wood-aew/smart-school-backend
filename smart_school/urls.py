from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('school_api/', include('school_api.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
