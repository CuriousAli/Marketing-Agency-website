from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('advercats/', advercats, name='adver_cats'),
    path('about_us/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('internet/', InternetAdv.as_view(), name='internet'),
    path('street/', StreetAdv.as_view(), name='street'),
    path('<slug:post_slug>/', ShowPost.as_view(), name='post')
]