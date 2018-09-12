from django.contrib import admin
from django.urls import path, include
from company.views import company_list, company_detail
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from . import views
from company.views import CompanyListView, FilteredCompanyTypeList, CompanyView




router = routers.DefaultRouter()
router.register('company', views.CompanyView)
router.register('zipcode', views.CompanyZipCodeView)
router.register('city', views.CompanyCityView)
router.register('companyname', views.CompanyNameView)
router.register('services', views.ServicesCompanyView)
router.register('foodandbev', views.FoodAndBevCompanyView)
router.register('entertainment', views.EntertainmentCompanyView)
router.register('products', views.ProductCompanyView)
router.register('religious', views.ReligiousServicesView)



urlpatterns = [
    path('', include(router.urls)),
    path('list/', CompanyListView.as_view(), name='list'),
    path('company_list/', views.company_list, name='company_list'),
    path('id/<int:id>/', views.company_detail, name='company_detail'),
    path('getlist/', FilteredCompanyTypeList.as_view(), name='get_querysetr')
]
