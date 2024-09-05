"""
recommender_system/home/urls.py

URL configuration for home application.
"""


from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]