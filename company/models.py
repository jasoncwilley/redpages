from django.db import models
from users.models import CustomUser

WEEKDAYS = [
  (1, "Monday"),
  (2, "Tuesday"),
  (3, "Wednesday"),
  (4, "Thursday"),
  (5, "Friday"),
  (6, "Saturday"),
  (7, "Sunday"),
]

class OpeningHours(models.Model):
    companyID = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True,)
    weekday = models.IntegerField(choices=WEEKDAYS)
    from_hour = models.TimeField()
    to_hour = models.TimeField()

    class Meta:
        ordering = ('weekday', 'from_hour')
        unique_together = ('weekday', 'from_hour', 'to_hour')

    def __unicode__(self):
        return u'%s: %s - %s' % (self.get_weekday_display(),
                                 self.from_hour, self.to_hour)

class CompanyID(models.Model):
    models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    companyID = models.AutoField(primary_key=True)
    company_name = models.CharField(blank=True, max_length=50)
    openning_times = models.ManyToManyField(OpeningHours)

    def __str__(self):
        return self.company_name

class CompanyLocation(models.Model):
    companyID = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True,)
    street_address = models.CharField(blank=True, max_length=50)
    city = models.CharField(blank=True, max_length=25)
    state = models.CharField(blank=True, max_length=25)
    zip_code = models.IntegerField(blank=True)
    comp_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    comp_latitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.companyID


class CompanyContacts(models.Model):
    companyID = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True,)
    company_email = models.EmailField(blank=True, max_length=35)
    company_twitter = models.CharField(blank=True, max_length=50)
    company_facebook = models.CharField(blank=True, max_length=50)
    company_instagram = models.CharField(blank=True, max_length=50)
    comapany_phone = models.CharField(blank=True, max_length=14)

    def __str__(self):
        return self.companyID
