
from django.urls import path, include
from rest_framework import routers

from .views import *

items_router = routers.DefaultRouter()

items_router.register(r"categories", CategoryListViewSet, basename="category")
items_router.register(r"main_category", MainPageCategoryListViewSet, basename="main_category")
items_router.register(r"subcategory_products", SubCategoryProductsViewSet, basename="subcategory_products")
items_router.register(r"product_detail", ProductDetailViewSet, basename="product_detail")
items_router.register(r"cart_add", CartViewSet, basename="cart_add")