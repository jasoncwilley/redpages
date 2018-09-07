from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework import routers
from . import views
from reviews.views import ReviewListView, RetrieveUpdateDestroyAPIView


urlpatterns = [
    path('review/', ReviewListView.as_view(), name='list'),
    path('list/', views.review_list, name='review_list'),
    path('<int:id>/', views.review_detail, name='review_detail'),
    path('detail/<int:id>/', RetrieveUpdateDestroyAPIView.as_view(),name='detail')
]
