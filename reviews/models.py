from django.db import models
import numpy as np
from company.models import CompanyByType
from datetime import datetime
import company
from company.models import CompanyByType

class Company(models.Model):
    id = models.IntegerField
    company_name = models.ForeignKey(company.models.CompanyByType,  on_delete=models.PROTECT)

    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)

    def __str__(self):
        return self.company_name.company_name


class Review(models.Model):
    ONE_STAR = 'one star'
    TWO_STARS = 'two stars'
    THREE_STARS = 'three stars'
    FOUR_STARS = 'four stars'
    FIVE_STARS = 'five stars'
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    FOOD_and_DRINKS = 'FOOD & DRINKS'
    ENTERTAINMENT = 'ENTERTAINMENT'
    SERVICES = 'SERVICES'
    PRODUCTS = 'PRODUCTS'
    RELIGIOUS_SERVICES = 'RELIGIOUS SERVICES'
    OTHER = 'OTHER'
    COMPANY_TYPE_CHOICES = (
        (FOOD_and_DRINKS, 'Food & Drinks'),
        (ENTERTAINMENT, 'Entertainment'),
        (SERVICES, 'Services'),
        (PRODUCTS, 'Products'),
        (RELIGIOUS_SERVICES, 'Religious Services'),
        (OTHER, 'Other'),
    )
    company_name = models.ForeignKey('company.CompanyByType', related_name='name', to_field='company_name', on_delete=models.CASCADE)
    company_type = models.CharField(choices=COMPANY_TYPE_CHOICES, max_length=25)
    first_name = models.CharField(blank=True, max_length=50)
    last_name = models.CharField(blank=True, max_length=25)
    comment = models.TextField(blank=True, max_length=500)
    rating = models.IntegerField(choices=RATING_CHOICES)
    pub_date =  models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name.company_name



ONE_STAR = 'one star'
TWO_STARS = 'two stars'
THREE_STARS = 'three stars'
FOUR_STARS = 'four stars'
FIVE_STARS = 'five stars'
RATING_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    )

FOOD_and_DRINKS = 'FOOD & DRINKS'
ENTERTAINMENT = 'ENTERTAINMENT'
SERVICES = 'SERVICES'
PRODUCTS = 'PRODUCTS'
RELIGIOUS_SERVICES = 'RELIGIOUS SERVICES'
OTHER = 'OTHER'
COMPANY_TYPE_CHOICES = (
    (FOOD_and_DRINKS, 'Food & Drinks'),
    (ENTERTAINMENT, 'Entertainment'),
    (SERVICES, 'Services'),
    (PRODUCTS, 'Products'),
    (RELIGIOUS_SERVICES, 'Religious Services'),
    (OTHER, 'Other'),
)
company_type = models.CharField(
    max_length=25,
    choices=COMPANY_TYPE_CHOICES,
    default=OTHER,
)
