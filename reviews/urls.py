from django.contrib import admin
from django.urls import path, include
from reviews.views import ReviewListView
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from . import views





router = routers.DefaultRouter()



urlpatterns = [
    path('review/', ReviewListView.as_view(), name='list')
    ]
