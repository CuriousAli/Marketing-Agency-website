# Generated by Django 3.1.7 on 2021-04-05 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertising', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adver',
            options={'ordering': ['actual', 'title'], 'verbose_name': 'Вид рекламы', 'verbose_name_plural': 'Вид рекламы'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Категорию', 'verbose_name_plural': 'категории'},
        ),
        migrations.AlterField(
            model_name='adver',
            name='actual',
            field=models.BooleanField(default=True, verbose_name='Актуальность'),
        ),
        migrations.AlterField(
            model_name='adver',
            name='addition_date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата добавления'),
        ),
        migrations.AlterField(
            model_name='adver',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertising.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='adver',
            name='description',
            field=models.TextField(default='Description for current adver', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='adver',
            name='image',
            field=models.ImageField(upload_to='pics/%Y/%m/%d', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='adver',
            name='price',
            field=models.CharField(max_length=10, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='adver',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='adver',
            name='title',
            field=models.CharField(max_length=255, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.TextField(db_index=True, max_length=25, unique=True, verbose_name='Название категории'),
        ),
    ]