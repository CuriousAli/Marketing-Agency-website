from django.db import models
from django.urls import reverse

'''Drafted models structure. You can see concept down below '''


class Adver(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=False, default="Description for current adver")
    image = models.ImageField(upload_to="pics/%Y/%m/%d")
    price = models.CharField(max_length=10)
    addition_date = models.DateField(auto_now_add=True)
    actual = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('type', kwargs={'type_id': self.pk})


class Category(models.Model):
    name = models.TextField(max_length=25, unique=True, db_index=True)

    def __str__(self):
        return self.name