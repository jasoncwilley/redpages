from django.contrib import admin
from . models import Review, Company

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('company', 'company_type', 'rating', 'first_name', 'last_name', 'comment', 'pub_date')
    list_filter = ['pub_date', 'first_name', 'last_name', ' company', 'company_type']
    search_fields = ['comment''pub_date', 'first_name', 'last_name', ' company', 'company_type']


admin.site.register(Review)
admin.site.register(Company)
