from django.shortcuts import render
from rest_framework import viewsets
from .models import CompanyByType, CompanyContacts, CompanyLocation
from .serializers import CompanyByTypeSerializer, CompanyContactsListSerializer, CompanyContactsDetailSerializer, CompanyContactsSerializer, CompanyLocationSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import DestroyAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
class CompanyContactsUpdateAPIView(RetrieveAPIView):
    queryset = CompanyContacts.objects.all()
    serializer_class = CompanyContactsDetailSerializer
    lookup_field = 'slug'
class CompanyContactsDetailAPIView(RetrieveAPIView):
    queryset = CompanyContacts.objects.all()
    serializer_class = CompanyContactsDetailSerializer
    lookup_field = 'slug'
class CompanyContactsDeleteAPIView(RetrieveAPIView):
    queryset = CompanyContacts.objects.all()
    serializer_class = CompanyContactsListSerializer
    lookup_field = 'slug'
class CompanyContactsListAPIView(ListAPIView):
    queryset = CompanyContacts.objects.all()
    serializer_class = CompanyContactsListSerializer
    lookup_field = 'slug'

class CompanyByTypeViewSet(viewsets.ModelViewSet):
    queryset= CompanyByType.objects.all()
    serializer_class = CompanyByTypeSerializer
    def list(self, request):
        queryset= CompanyByType.objects.all()
        serializer = CompanyByTypeSerializer(queryset, many=True)
        return Response(serializer.data)

def companycontacts_update(request, slug=None):
    instance = get_object_or_404(CompanyByType, slug=slug)
    form = CompanyContactsForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        messages.success(request, "<a href='#'>Saved", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'company_name': instance.company_name,
        'company_email': instance.company_email,
        'company_twitter': instance.company_twitter,
        'company_facebook': instance.company_facebook,
        'company_instagram': instance.company_instagram,
        'instance': instance,
        'form': form,
    }
    return render(request, companycontactsform.html, context)




@csrf_exempt
def companybytype_list(request):
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
def companybytype_detail(request, id):
    try:
        companybytype = CompanyByType.objects.get(id=id)
    except CompanyByType.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':

        serializer = CompanyByTypeSerializer(companybytype)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CompanyByTypeSerializer(companybytype, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        companybytype.delete()
        return HttpResponse(status=204)




class CompanyContactsViewSet(ModelViewSet):
    queryset = CompanyContacts.objects.all()
    serializer_class = CompanyContactsSerializer
    def list(self, request):
        queryset = CompanyContacts.objects.all()
        serializer = CompanyContactsSerializer(queryset, many=True)
        return Response(serializer.data)
@csrf_exempt
def companycontacts_list(request):
    if request.method == 'GET':
        queryset = CompanyContacts.objects.all()
        serializer = CompanyContactsSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CompanyContactsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
@csrf_exempt
def companycontacts_detail(request, id):
    try:
        companycontacts = CompanyContacts.objects.get(id=id)
    except CompanyContacts.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':

        serializer = CompanyContactsSerializer(companycontacts)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CompanyContactsSerializer(companycontacts, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        companycontacts.delete()
        return HttpResponse(status=204)

class CompanyLocationViewSet(ModelViewSet):
    queryset = CompanyLocation.objects.all()
    serializer_class = CompanyLocationSerializer
    def list(self, request):
        queryset = CompanyLocation.objects.all()
        serializer = CompanyLocationSerializer(queryset, many=True)
        return Response(serializer.data)
@csrf_exempt
def companylocation_list(request):
    if request.method == 'GET':
        queryset = CompanyLocation.objects.all()
        serializer = CompanyLocationSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CompanyLocationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
@csrf_exempt
def companylocation_detail(request, id):
    try:
        companylocation = CompanyLocation.objects.get(id=id)
    except CompanyLocation.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':

        serializer = CompanyLocationSerializer(companylocation)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CompanylocationSerializer(companylocation, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        companylocation.delete()
        return HttpResponse(status=204)
