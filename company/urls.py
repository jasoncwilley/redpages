from django.contrib import admin
from django.urls import path, include
from . import views
from .views import CompanyContactsListAPIView, CompanyContactsUpdateAPIView
from rest_framework.routers import DefaultRouter
from rest_framework import routers



router = routers.DefaultRouter()
router.register('CompanyByType', views.CompanyByTypeViewSet)
router.register('CompanyContacts', views.CompanyContactsViewSet)
router.register('CompanyLocation', views.CompanyLocationViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('companycontactslistview/', CompanyContactsListAPIView.as_view(), name='list'),
    path('companycontacts/edit/<slug:slug>/', CompanyContactsUpdateAPIView.as_view(), name='update'),

    path('companytype_list/', views.companybytype_list, name='companybytype_list'),
    path('<int:id>/', views.companybytype_detail, name='companybytype_detail'),
    path('contacts_list/', views.companycontacts_list, name='companycontacts_list'),
    path('contacts/<int:id>/', views.companycontacts_detail, name='companycontacts_detail'),
    path('location_list/', views.companylocation_list, name='companylocation_list'),
    path('location/<int:id>/', views.companylocation_detail, name='companylocation_detail'),

]
