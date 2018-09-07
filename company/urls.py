from django.contrib import admin
from django.urls import path, include
from company.views import company_list, company_detail
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from . import views
from company.views import CompanyListView




router = routers.DefaultRouter()
router.register('CompanyByType', views.CompanyViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('list/', CompanyListView.as_view(), name='list'),
    
    path('company_list/', views.company_list, name='company_list'),
    path('<int:id>/', views.company_detail, name='company_detail'),


]
