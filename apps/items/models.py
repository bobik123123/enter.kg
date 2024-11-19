from django.db import models
from ..utilts import upload_to_common


class Category(models.Model):
    name = models.CharField("название категории", max_length=50)
    image = models.ImageField("изображение категории", upload_to=upload_to_common, null=True, blank=True)


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
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="product", default=1)
    name = models.CharField("название продукта", max_length=255, null=True, blank=True)
    image = models.ImageField("изображение продукта", upload_to=upload_to_common, null=True, blank=True)
    price = models.PositiveIntegerField("Цена", null=True, blank=True)
    amount = models.PositiveIntegerField("Количество товара", null=True, blank=True)

    class Meta:
        verbose_name = "Продукты"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name


