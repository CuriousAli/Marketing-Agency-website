from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render
from .templates import *



'''
This project bases on MTV pattern. Views in final must be classes(ofc if funcion can't solve task by few strings of code)
, but first of all, step by step i will create functions and after replace them on classes
'''


def mainpage(request):
    return render(request, 'advertising/mainpage.html')

def advercats(request):
    return render(request, 'advertising/advercats.html')

def pageNotFound(request, exception):
    raise HttpResponseNotFound('<h1>Страница не найдена</h1>')

