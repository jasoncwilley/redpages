from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import CompanyByType, CompanyLocation, CompanyContacts



admin.site.register(CompanyByType)
admin.site.register(CompanyLocation)
admin.site.register(CompanyContacts)
