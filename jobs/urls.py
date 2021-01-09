from django.urls import path

from .views import *
app_name = 'jobs'

urlpatterns = [
    path('', index),
    path('2', index2)
]
