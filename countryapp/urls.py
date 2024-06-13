from django.urls import path
from countryapp import views

urlpatterns=[
    path('', views.display, name='display'),
]
