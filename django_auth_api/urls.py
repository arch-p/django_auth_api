
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path(''),
    path('api/', include('djoser.urls')),
    path('api/', include('users.urls')),
]
