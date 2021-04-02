from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='main'),
    path('advercats/', advercats, name='advercats'),
]