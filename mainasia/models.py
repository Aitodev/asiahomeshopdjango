from django.db import models
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Category(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=200)
    slug_category = models.SlugField(verbose_name='URL (добавляется автоматически)', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):

    RATE_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ]
    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )

    name = models.CharField(verbose_name='Имя', max_length=200)
    img1 = models.ImageField(verbose_name='Изображение 1', upload_to='static/img/products/')
    img2 = models.ImageField(verbose_name='Изображение 2', upload_to='static/img/products/')
    slug_product = models.SlugField(verbose_name='URL (добавляется автоматически)', unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    price_disc = models.DecimalField(verbose_name='Цена со скидкой', max_digits=7, decimal_places=2, null=True,
                                     blank=True)
    discount = models.DecimalField(verbose_name='Размер скидки', max_digits=2, decimal_places=0, null=True, blank=True)
    new = models.BooleanField(verbose_name='Новый товар')
    rating = models.CharField(verbose_name='Рейтинг', max_length=1, choices=RATE_CHOICES, blank=True)
    describe = models.TextField(verbose_name='Описание')
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    objects = models.Manager()
    published = PublishedManager()
    date = models.DateTimeField(verbose_name='Дата добавления', auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Applications(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=200)
    mail = models.CharField(verbose_name='Почта', max_length=200)
    comment = models.CharField(verbose_name='Коммент', max_length=200)
    date = models.DateTimeField(verbose_name='Дата', auto_now_add=True, null=True)

    def __str__(self):
        return self.mail

    class Meta:
        verbose_name = 'Заявка cо страницы контактов'
        verbose_name_plural = 'Заявка со страницы контактов'


class Banners(models.Model):
    title1 = models.CharField(verbose_name='Мини заголовок', max_length=200, blank=True)
    titlemain = models.CharField(verbose_name='Главный заголовок', max_length=200)
    imgbanner = models.ImageField(verbose_name='Изображение', upload_to='static/img/banners/')
    slug = models.CharField(verbose_name='Ссылка на товар', max_length=200, blank=True)

    def __str__(self):
        return self.titlemain

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'

