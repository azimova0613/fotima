from django.urls import path
from .views import *

urlpatterns=[
    path('index/',Index),
    path('shop/',shop),
    path('contact/',contact),
    path('blogsingle/',blogsingle),
    path('gallery/',gallery),
    path('team/',team),
    path('service/',service),
    path('shopsingle/',shopsingle),
    path('errorpage/',errorpage),
    path('teamsingle/',teamsingle),
]