from django.db import models



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


class CompanyByType(models.Model):

    company_name = models.CharField(max_length=50)


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


    def __str__(self):
        return self.company_name


class CompanyLocation(models.Model):
    company_name = models.CharField(max_length=50)
    street_address = models.CharField(blank=True, max_length=50)
    city = models.CharField(blank=True, max_length=25)
    state = models.CharField(blank=True, max_length=25)
    zip_code = models.CharField(blank=True, max_length=5)
    comp_longitude = models.DecimalField(blank=True, max_digits=9, decimal_places=6)
    comp_latitude = models.DecimalField(blank=True, max_digits=9, decimal_places=6)
    def __str__(self):
        return self.company_name


class CompanyContacts(models.Model):
    company_name = models.CharField(max_length=50)
    company_email = models.EmailField(blank=True, max_length=35)
    company_twitter = models.CharField(blank=True, max_length=50)
    company_facebook = models.CharField(blank=True, max_length=50)
    company_instagram = models.CharField(blank=True, max_length=50)

    def __str__(self):
        return self.company_name
