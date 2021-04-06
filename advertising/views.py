from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from .templates import *
from .models import *


'''
This project bases on MTV pattern. Views in final must be classes(ofc if function can't solve task by few strings of code)
, but first of all, step by step i will create functions and after replace them on classes
'''


menu = [{'title': 'Реклама', 'url_name': 'adver_cats'},
        {'title': 'О нас', 'url_name': 'about'},
        {'title': 'Связь', 'url_name': 'contacts'}
]


def index(request):
    context = {
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'advertising/index.html', context=context)


def advercats(request):
    context = {
        'menu': menu,
        'title': 'Реклама'
    }
    return render(request, 'advertising/advercats.html', context=context)


def internet(request):
    posts = Adver.objects.filter(cat_id=1)
    context = {
        'menu': menu,
        'posts': posts,
        'title': 'Реклама в интернете'
    }
    return render(request, 'advertising/internet.html', context=context)


def street(request):
    posts = Adver.objects.filter(cat_id=2)
    context = {
        'menu': menu,
        'posts': posts,
        'title': 'Наружная реклама'
    }
    return render(request, 'advertising/street.html', context=context)

def show_post(request, post_slug):
    post = get_object_or_404(Adver, post_slug)
    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
    }
    return render(request, 'advertising/post.html', context=context)



def about(request):
    context = {
        'menu': menu,
        'title': 'О нас'
    }
    return render(request, 'advertising/about.html', context=context)


def contacts(request):
    context = {
        'menu': menu,
        'title': 'Связь'
    }
    return render(request, 'advertising/contacts.html', context=context)


def pageNotFound(request, exception):
    raise HttpResponseNotFound('<h1>Страница не найдена</h1>')

