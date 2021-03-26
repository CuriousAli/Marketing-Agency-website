from django.db import models

'''Drafted models structure. You can see concept down below '''
class Adver(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=False, default="Description for current adver")
    image = models.ImageField(upload_to="pics/%Y/%m/%d")
    price = models.CharField(max_length=10)
    addition_date = models.DateField(auto_now_add=True)
    actual = models.BooleanField(default=True)
