from django.shortcuts import render
from rest_framework import viewsets
from .models import Dish, Category, DishSize
from .serializers import DishSerializer, CategorySerializer, DishSizeSerializer


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DishSizeViewSet(viewsets.ModelViewSet):
    queryset = DishSize.objects.all()
    serializer_class = DishSizeSerializer






