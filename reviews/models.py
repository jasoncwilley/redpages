from django.db import models
import numpy as np
from company.models import CompanyByType
from datetime import datetime



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

class Review(models.Model):
    company_name = models.ForeignKey(CompanyByType, on_delete=models.CASCADE)
    first_name = models.CharField(blank=True, max_length=50)
    last_name = models.CharField(blank=True, max_length=25)
    comment = models.TextField(blank=True, max_length=500)
    rating = models.IntegerField(choices=RATING_CHOICES)
    pub_date = models.DateTimeField('date created', default=datetime.now())
