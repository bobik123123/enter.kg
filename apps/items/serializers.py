from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name',  'product_count']


class MainPageCategorySerializer(serializers.ModelSerializer):
    product_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'product_count']


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'image', 'price']


class SubCategoryProductsSerializer(serializers.ModelSerializer):
    product = ProductsSerializer(many=True)
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'image', 'product']


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'image', 'price']


class CartItemSerializier(serializers.ModelSerializer):
    class Meta:
        model = CartItem


class CartSerializer(serializers.ModelSerializer):
    cart_item = CartItemSerializier(many=True)
    class Meta:
        model = Cart
        fields = ('id', 'cart_item')

