from django.db import models
from django.urls import reverse

'''Drafted models structure. You can see concept down below '''


class Adver(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Слаг')
    description = models.TextField(blank=False, default="Description for current adver", verbose_name='Описание')
    image = models.ImageField(upload_to="pics/%Y/%m/%d", verbose_name='Изображение')
    price = models.CharField(max_length=10, verbose_name='Цена')
    addition_date = models.DateField(auto_now_add=True, verbose_name='Дата добавления')
    actual = models.BooleanField(default=True, verbose_name='Актуальность')
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('type', kwargs={'slug_id': self.slug})

    # Created this class for customize admin panel.
    class Meta:
        verbose_name = 'Вид рекламы'
        verbose_name_plural = 'Вид рекламы'
        ordering = ['actual', 'title']


class Category(models.Model):
    name = models.TextField(max_length=25, unique=True, db_index=True, verbose_name='Название категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'категории'
        ordering = ['name']