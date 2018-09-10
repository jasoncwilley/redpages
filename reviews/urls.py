from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework import routers
from . import views
from reviews.views import ReviewList, ReviewViewSet, ReviewListView, RetrieveUpdateDestroyAPIView

router = routers.DefaultRouter()
router.register('Review', views.ReviewViewSet)
router.register('reviews', views.ReviewList)
urlpatterns = [
    path('', include(router.urls)),
    path('postreviews/', ReviewListView.as_view(), name='post'),
    path('getreviews/', ReviewListView.as_view(), name='list'),
    path('list/', views.review_list, name='review_list'),
    path('<int:id>/', views.review_detail, name='review_detail'),
    path('detail/<int:id>/', RetrieveUpdateDestroyAPIView.as_view(),name='detail'),
    path('review_list/', views.review_list, name='review_list'),
    path('review/<int:review_id>/', views.review_detail, name='review_detail'),
    path('company', views.company_detail, name='company_detail'),
    path('company/<int:company_id>', views.company_detail, name='company_detail'),
    path('company/<int:company_id>/add_review/', views.add_review, name='add_review')
]
