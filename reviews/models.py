from django.db import models
import numpy as np
from company.models import CompanyByType

class CompanyReviews(models.Model):
    company_name = models.ForeignKey(CompanyByType, on_delete=models.CASCADE)


    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)

    def __str__(self):
        return self.company_name

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

class Review(models.Model):
    Companyreview= models.CharField(max_length=500)
    def __str__(self):
        return self.companyreview.company_name

    first_name = models.CharField(blank=True, max_length=50)
    last_name = models.CharField(blank=True, max_length=25)
    comment = models.TextField(blank=True, max_length=500)
    rating = models.IntegerField(choices=RATING_CHOICES)
    pub_date = models.DateTimeField('date published')
