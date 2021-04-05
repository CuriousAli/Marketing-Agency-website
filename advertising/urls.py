from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('advercats/', advercats, name='adver_cats'),
    path('about_us/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('internet/', internet, name='internet'),
    path('street/', street, name='street')
]