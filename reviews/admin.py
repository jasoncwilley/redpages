from django.contrib import admin
from . models import CompanyReviews, Review

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('companyname', 'rating', 'first_name', 'last_name', 'comment', 'pub_date')
    list_filter = ['pub_date', 'first_name', 'last_name']
    search_fields = ['comment']

admin.site.register(CompanyReviews)
admin.site.register(Review)
