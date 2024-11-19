from rest_framework import routers

from .views import *

items_router = routers.DefaultRouter()

items_router.register(r"category", CategoryViewSet, basename="category")