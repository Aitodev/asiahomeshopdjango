# Generated by Django 3.0 on 2020-09-18 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainasia', '0005_auto_20200918_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img2',
            field=models.ImageField(blank=True, upload_to='static/img/products/', verbose_name='Изображение 2'),
        ),
        migrations.AlterField(
            model_name='product',
            name='new',
            field=models.BooleanField(blank=True, verbose_name='Новый товар'),
        ),
    ]
