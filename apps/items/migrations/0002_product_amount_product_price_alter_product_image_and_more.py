# Generated by Django 5.1.3 on 2024-11-19 11:47

import apps.utilts
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='amount',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество товара'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=apps.utilts.upload_to_common, verbose_name='изображение продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='название продукта'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=apps.utilts.upload_to_common, verbose_name='изображение подкатегории'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='название подкатегории'),
        ),
    ]
