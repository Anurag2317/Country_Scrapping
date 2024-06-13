from django.db import models


class Country(models.Model):
    country_name = models.CharField(primary_key=True, max_length=50)
    country_code = models.CharField(max_length=30)
    iso_codes = models.CharField(max_length=30)
    population = models.CharField(max_length=50)
    area_km2 = models.CharField(max_length=50)
    gdp_usd = models.CharField(max_length=30)
    capital = models.CharField(max_length=50)
