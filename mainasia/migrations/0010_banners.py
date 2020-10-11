# Generated by Django 3.0 on 2020-10-11 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainasia', '0009_auto_20200918_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(blank=True, max_length=200, verbose_name='Мини заголовок')),
                ('titlemain', models.CharField(max_length=200, verbose_name='Главный заголовок')),
                ('imgbanner', models.ImageField(upload_to='static/img/banners/', verbose_name='Изображение')),
                ('slug', models.CharField(blank=True, max_length=200, verbose_name='Ссылка на товар')),
            ],
            options={
                'verbose_name': 'Баннер',
                'verbose_name_plural': 'Баннеры',
            },
        ),
    ]