from django.contrib import admin
from .models import Category, Product, Applications, Banners


class CategoryConfig(admin.ModelAdmin):
    fields = ('name', 'slug_category')
    list_display = ('name', )
    prepopulated_fields = {'slug_category': ('name',)}


admin.site.register(Category, CategoryConfig)


class ProductConfig(admin.ModelAdmin):
    fields = ('name', 'category', 'img1', 'img2', 'price', 'price_disc', 'discount', 'new', 'rating', 'slug_product', 'describe')
    list_display = ('name', 'category', 'price', 'describe', 'date')
    prepopulated_fields = {'slug_product': ('name',)}


admin.site.register(Product, ProductConfig)


class ApplicationsConfig(admin.ModelAdmin):
    fields = ('mail', 'name', 'comment')
    list_display = ('name', 'mail', 'date', 'comment')
    admin.site.register(Applications)


class BannersConfig(admin.ModelAdmin):
    fields = ('title1', 'titlemain', 'imgbanner', 'slug')
    list_display = ('titlemain', 'slug')


admin.site.register(Banners, BannersConfig)
