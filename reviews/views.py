from django.shortcuts import get_object_or_404, render
from reviews.models import Review, Company
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from company.models import CompanyByType
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from reviews.serializers import ReviewSerializer,  ReviewListSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import generics
from django.http import HttpResponseRedirect

from .forms import ReviewForm
import datetime

class ReviewList(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer



def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'reviews/review_list.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})

def company_list(request):
    company_list = Company.objects.order_by('-name')
    context = {'company_list':company_list}
    return render(request, 'reviews/company_list.html', context)


def company_detail(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    return render(request, 'reviews/company_list.html', {'company': company})


def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'reviews/review_list.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})


def company_list(request):
    company_list = Company.objects.order_by('-name')
    context = {'company_list':company_list}
    return render(request, 'reviews/company_list.html', context)


def company_detail(request, company_id):
    company = get_object_or_404(company, pk=company_id)
    form = ReviewForm()
    return render(request, 'reviews/company_detail.html', {'company': company, 'form': form})


def add_review(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        user_name = form.cleaned_data['user_name']
        review = Review()
        review.company = company
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('reviews:company_detail', args=(company.id,)))

    return render(request, 'reviews/company_detail.html', {'company': company, 'form': form})

class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    def list(self, request):
        queryset = Review.objects.all()
        serializer = ReviewSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def get(self, request):
         reviews = Review.objects.all()
         serializer = ReviewSerializer(reviews, many=True)
         return Response(serializer.data)



class ReviewListView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    queryset =Review.objects.all()

class ReviewDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'


@csrf_exempt
def review_list(self, request):
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
