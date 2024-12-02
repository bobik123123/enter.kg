from django.db.models import Sum, Count
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from .serializers import *
from .models import *

class CategoryListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def list(self, request, *args, **kwargs):
        categories = self.get_queryset().annotate(
            product_count=Count('subcategory__product')
        )
        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data)


class MainPageCategoryListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = MainPageCategorySerializer
    def list(self, request, *args, **kwargs):
        categories = self.get_queryset().annotate(
            product_count=Count('subcategory__product')
        )
        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data)

class SubCategoryProductsViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryProductsSerializer


class ProductDetailViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class CartViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CartSerializer

    def create(self, request, *args, **kwargs):
        user = request.data.get("user")
        items = request.data.get("items", [])

        if User.objects.filter(id=user):
            user = User.objects.get(id=user)
        else:
            return Response({"error": "пользователь не найден"})



