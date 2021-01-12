from django.urls import path, re_path
from .views import *
app_name = 'jobs'


urlpatterns = [
    path('1/', index),
    path('2/', index2),
    path('3/', Test.as_view()),
]
