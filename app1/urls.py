from django.urls import path
from app1.views import *

app_name='app1'

urlpatterns=[
    path('new1/',new1,name='new1'),
]