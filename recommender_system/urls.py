"""
recommender_system/recommender_system/urls.py

URL configuration for recommender_system project.
"""


from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    
]
