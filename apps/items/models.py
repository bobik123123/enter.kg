from django.db import models

from ..users.models import User
from ..utilts import upload_to_common


class Category(models.Model):
    name = models.CharField("название категории", max_length=50)
    image = models.ImageField("изображение категории", upload_to=upload_to_common)


    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategory")
    name = models.CharField("название подкатегории", max_length=50, null=True, blank=True)
    image = models.ImageField("изображение подкатегории", upload_to=upload_to_common, null=True, blank=True)

    class Meta:
        verbose_name = "Подкатегории"
        verbose_name_plural = "подкатегории"

    def __str__(self):
        return self.name


class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="product")
    name = models.CharField("название продукта", max_length=255, null=True, blank=True)
    image = models.ImageField("изображение продукта", upload_to=upload_to_common, null=True, blank=True)
    price = models.PositiveIntegerField("Цена", null=True, blank=True)
    amount = models.PositiveIntegerField("Количество товара", null=True, blank=True)


    class Meta:
        verbose_name = "Продукты"
        verbose_name_plural = "Продукты"


    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart")

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"


    def __str__(self):
        return self.user


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_item")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cart_item")

    class Meta:
        verbose_name = "Продукт в корзине"
        verbose_name_plural = "Продукт в корзине"

    def __str__(self):
        return self.product.name


