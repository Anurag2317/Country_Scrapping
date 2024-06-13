from django.contrib import admin
from countryapp.models import Country

# Register your models here.
class CountryAdmin(admin.ModelAdmin):
    list_display=['country_name','country_code','iso_codes','population','area_km2','gdp_usd','capital']

admin.site.register(Country,CountryAdmin)