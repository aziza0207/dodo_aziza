from django.db.models import QuerySet, F, Sum
from django.shortcuts import render
from rest_framework import viewsets
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        queryset: QuerySet[Cart] = super().get_queryset()
        queryset = queryset.annotate(cost=F("cartitem__amount")*F("cartitem__dish_size__price")).\
            values("id").annotate(total_cost=Sum("cost"))
        return queryset


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def get_queryset(self):
        queryset: QuerySet[CartItem] = super().get_queryset()
        queryset = queryset.annotate(cost=F("amount") * F("dish_size__price"))
        return queryset

