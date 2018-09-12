from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from company.models import CompanyByType
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from company.serializers import CompanyTypeSerializer, CompanyByTypeSerializer, CompanySerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from django.db.models import Q
import django_filters.rest_framework
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

#Search for Company that Provide Services
#http://127.0.0.1:8000/religious?q=
class ReligiousServicesView(viewsets.ModelViewSet):
    queryset = CompanyByType.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['company_type',]
    def get_queryset(self, *args, **kwargs):
        queryset_list = CompanyByType.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(company_type__icontains=query)
                ).distinct()
        return queryset_list

#Search for Company that Provide Services
#http://127.0.0.1:8000/services?q=
class ServicesCompanyView(viewsets.ModelViewSet):
    queryset = CompanyByType.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['company_type',]
    def get_queryset(self, *args, **kwargs):
        queryset_list = CompanyByType.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(company_type__icontains=query)
                ).distinct()
        return queryset_list

#Search for Company that Sale Products
#http://127.0.0.1:8000/products?q=
class ProductCompanyView(viewsets.ModelViewSet):
    queryset = CompanyByType.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['company_type',]
    def get_queryset(self, *args, **kwargs):
        queryset_list = CompanyByType.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(company_type__icontains=query)
                ).distinct()
        return queryset_list


#Search for an Entertainmnt Company
#http://127.0.0.1:8000/entertainmnt/?q=
class EntertainmentCompanyView(viewsets.ModelViewSet):
    queryset = CompanyByType.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['company_type',]
    def get_queryset(self, *args, **kwargs):
        queryset_list = CompanyByType.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(company_type__icontains=query)
                ).distinct()
        return queryset_list


#Search for a Company by Company Type
#http://127.0.0.1:8000/foodandbev/?q=
class FoodAndBevCompanyView(viewsets.ModelViewSet):
    queryset = CompanyByType.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['company_type',]
    def get_queryset(self, *args, **kwargs):
        queryset_list = CompanyByType.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(company_type__icontains=query)
                ).distinct()
        return queryset_list


#Search for a Company by Comapny Name
#http://127.0.0.1:8000/comapny/?q=
class CompanyNameView(viewsets.ModelViewSet):
    queryset = CompanyByType.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['company_name',]
    def get_queryset(self, *args, **kwargs):
        queryset_list = CompanyByType.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(company_name__icontains=query)
                ).distinct()
        return queryset_list

#Search for a Company by City
#http://127.0.0.1:8000/city/?q=
class CompanyCityView(viewsets.ModelViewSet):
    queryset = CompanyByType.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['city',]
    def get_queryset(self, *args, **kwargs):
        queryset_list = CompanyByType.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(city__icontains=query)
                ).distinct()
        return queryset_list
#Search for a Company by Zip CompanyZipCodeView
#http://127.0.0.1:8000/zipcode/?q=
class CompanyZipCodeView(viewsets.ModelViewSet):
    queryset = CompanyByType.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['zip_code',]
    def get_queryset(self, *args, **kwargs):
        queryset_list = CompanyByType.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(zip_code__icontains=query)
                ).distinct()
        return queryset_list
class CompanyView(viewsets.ModelViewSet):
    queryset = CompanyByType.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['id', 'company_name', 'company_type',
    'company_twitter', 'company_facebook',
    'company_instagram', 'street_address',
    'city', 'state', 'zip_code',]
    def get_queryset(self, *args, **kwargs):
        queryset_list = CompanyByType.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(company_name__icontains=query) |
                Q(company_email__icontains=query) |
                Q(company_type__icontains=query) |
                Q(street_address__icontains=query) |
                Q(city__icontains=query) |
                Q(state__icontains=query) |
                Q(zip_code__icontains=query)
                ).distinct()
        return queryset_list



class CompanyListView(ListAPIView, CreateAPIView):
    serializer_class = CompanySerializer
    #queryset = CompanyByType.objects.all()

    def get_queryset(self, *args, **kwargs):
        queryset = CompanyByType.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(company_name__icontains=query)|
                Q(company_email__icontains=query)|
                Q(company_twitter__icontains=query)|
                Q(company_facebook__icontains=query)|
                Q(company_instagram__icontains=query)|
                Q(street_address__icontains=query)|
                Q(city__icontains=query)|
                Q(state__icontains=query)|
                Q(zip_code__icontains=query)|
                Q(comp_longitude__icontains=query)|
                Q(comp_latitude__icontains=query)
                ).distinct
        return queryset_list
class FilteredCompanyTypeList(generics.ListAPIView):
    serializer_class = CompanyTypeSerializer
    queryset = CompanyByType.objects.all()
    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get('Q')
        queryset = CompanyByType.objects.all()
        queryset_list = CompanyByType.objects.all()
        serializer = CompanyByTypeSerializer(queryset_list, many=True)
        if query:
            queryset_list = queryset.filter(
            Q(company_name__icontains=query)|
            Q(company_type__icontains=query)|
            Q(company_facebook__icontains=query)|
            Q(company_instagram__icontains=query)|
            Q(street_address__icontains=query)|
            Q(city__icontains=query)|
            Q(state__icontains=query)|
            Q(zip_code__icontains=query)|
            Q(comp_longitude__icontains=query)|
            Q(comp_latitude__icontains=query)).distinct
            return JsonResponse(queryset_list, safe=False)




@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        queryset = CompanyByType.objects.all()
        serializer = CompanyByTypeSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CompanyByTypeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def company_detail(request, id):
    try:
        companydetails = CompanyByType.objects.get(id=id)
    except CompanyByType.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = CompanyByTypeSerializer(companydetails)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CompanyByTypeSerializer(companydetails, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        companydetails.delete()
        return HttpResponse(status=204)
