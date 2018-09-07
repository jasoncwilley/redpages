from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from company.models import CompanyByType
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from reviews.serializers import CompanyReviewsSerializer, ReviewSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from reviews.models import CompanyReviews, Review


class ReviewListView(ListAPIView, CreateAPIView):
    serializer_class = ReviewSerializer
    queryset = CompanyReviews.objects.all()
