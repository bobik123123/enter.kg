from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.response import Response

from .models import *
from .serializers import *

class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer