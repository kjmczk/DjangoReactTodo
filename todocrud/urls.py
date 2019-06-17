"""
todocrud URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('frontend.urls')),
    path('api/', include('todos.urls')),
    path('admin/', admin.site.urls),
]
