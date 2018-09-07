from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from company.models import CompanyByType
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from reviews.serializers import ReviewSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import generics
from reviews.models import  Review

class ReviewListView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    queryset =Review.objects.all()



@csrf_exempt
def review_list(request):
    if request.method == 'GET':
        queryset = Review.objects.all()
        serializer = ReviewSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
@csrf_exempt
def review_detail(request, id):
    try:
        reviewdetails = Review.objects.get(id=id)
    except ReviewDoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ReviewSerializer(reviewdetails)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ReviewSerializer(companybytype, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        review.delete()
        return HttpResponse(status=204)
