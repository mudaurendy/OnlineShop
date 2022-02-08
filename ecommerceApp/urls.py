

from shop.views import HomePageView
from.views import *
from django.urls import path, include



app_name = 'shop'

urlpatterns=[
path('', HomePageView, name='shop'),
path('', include('shop.urls', namespace='shop'))
]