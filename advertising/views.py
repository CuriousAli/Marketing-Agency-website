from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import *


'''
This project bases on MTV pattern. Views in final must be classes(ofc if function can't solve task by few strings of code)
, but first of all, step by step i will create functions and after replace them on classes
'''

# List of sections on website. Main menu in base.html menu block
menu = [{'title': 'Реклама', 'url_name': 'adver_cats'},
        {'title': 'О нас', 'url_name': 'about'},
        {'title': 'Связь', 'url_name': 'contacts'}
]


# View function of starting page
def index(request):
    context = {
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'advertising/index.html', context=context)

# View function with choice type of advers (internet or 'street' adv)
def advercats(request):
    context = {
        'menu': menu,
        'title': 'Реклама'
    }
    return render(request, 'advertising/advercats.html', context=context)


# Class view instead of function 'internet' with the same abilities.
class InternetAdv(ListView):
    paginate_by = 3
    posts = Adver
    template_name = 'advertising/internet.html'
    context_object_name = 'posts'
    extra_context = {'title': 'Реклама в интернете'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context

    def get_queryset(self):
        return Adver.objects.filter(cat_id=1)


# Class view instead of function 'street' with the same abilities.
class StreetAdv(ListView):
    paginate_by = 3
    posts = Adver
    template_name = 'advertising/street.html'
    context_object_name = 'posts'
    extra_context = {'title': 'Наружная реклама'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context

    def get_queryset(self):
        return Adver.objects.filter(cat_id=2)

'''def internet(request):
    posts = Adver.objects.filter(cat_id=1)
    context = {
        'menu': menu,
        'posts': posts,
        'title': 'Реклама в интернете'
    }
    return render(request, 'advertising/internet.html', context=context)'''


'''def street(request):
    posts = Adver.objects.filter(cat_id=2)
    context = {
        'menu': menu,
        'posts': posts,
        'title': 'Наружная реклама'
    }
    return render(request, 'advertising/street.html', context=context)'''

# Class view instead of function 'show_post' with the same abilities.
class ShowPost(DetailView):
    model = Adver
    template_name = 'advertising/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context

'''def show_post(request, post_slug):
    post = get_object_or_404(Adver, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
    }
    return render(request, 'advertising/post.html', context=context)'''


# View function of introducing of company
def about(request):
    context = {
        'menu': menu,
        'title': 'О нас'
    }
    return render(request, 'advertising/about.html', context=context)

# View function with contact information
def contacts(request):
    context = {
        'menu': menu,
        'title': 'Связь'
    }
    return render(request, 'advertising/contacts.html', context=context)

# Function for incorrect requests
def pageNotFound(request, exception):
    raise HttpResponseNotFound('<h1>Страница не найдена</h1>')

