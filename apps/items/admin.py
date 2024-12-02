from django.contrib import admin

from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


class CartProduct(admin.TabularInline):
    model = CartItem


@admin.register(Cart)
class ProductAdmin(admin.ModelAdmin):
    inlines = [CartProduct]

