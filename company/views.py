from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from company.models import CompanyByType
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from company.serializers import CompanyByTypeSerializer, CompanySerializer
from rest_framework.generics import ListAPIView, CreateAPIView


class CompanyListView(ListAPIView, CreateAPIView):
    serializer_class = CompanyByTypeSerializer
    queryset = CompanyByType.objects.all()




class CompanyViewSet(ModelViewSet):
    queryset = CompanyByType.objects.all()
    serializer_class = CompanyByTypeSerializer

    def list(self, request):
        queryset = CompanyByType.objects.all()
        serializer = CompanyByTypeSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)


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
