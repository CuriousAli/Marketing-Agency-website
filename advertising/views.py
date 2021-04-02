from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render
from .templates import *
from .models import *


'''
This project bases on MTV pattern. Views in final must be classes(ofc if funcion can't solve task by few strings of code)
, but first of all, step by step i will create functions and after replace them on classes
'''


menu = ["Рекламные решения", "О нас", "Контактная информация"]

def index(request):
    types = Adver.objects.all()
    return render(request, 'advertising/index.html', {'types': types, 'menu': menu, 'title': 'Главная страница'})


def advercats(request):
    return render(request, 'advertising/advercats.html', {'menu': menu, 'title': 'Рекламные решения'})


def pageNotFound(request, exception):
    raise HttpResponseNotFound('<h1>Страница не найдена</h1>')

