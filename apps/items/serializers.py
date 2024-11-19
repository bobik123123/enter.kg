# serializers.py
from rest_framework import serializers
from .models import Category, SubCategory, Product



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'image',]
