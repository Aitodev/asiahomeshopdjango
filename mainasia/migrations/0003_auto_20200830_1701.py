# Generated by Django 3.0 on 2020-08-30 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainasia', '0002_product_describe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='describe',
            field=models.TextField(max_length=250, verbose_name='Описание'),
        ),
    ]