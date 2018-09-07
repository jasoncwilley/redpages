from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework import routers
from . import views
from reviews.views import ReviewListView





router = routers.DefaultRouter()



urlpatterns = [
    path('review/', ReviewListView.as_view(), name='list')
    ]
