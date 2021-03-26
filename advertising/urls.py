from django.urls import path

from .views import *

urlpatterns = [
    path('', mainpage, name='main'),
    path('advercats', advercats, name='advercats'),
]