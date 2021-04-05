from django.contrib import admin

from .models import *


class AdverAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'price', 'actual', 'cat')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'cat', 'slug', 'actual')
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Adver, AdverAdmin)
admin.site.register(Category, CategoryAdmin)