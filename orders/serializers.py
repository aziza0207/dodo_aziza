from rest_framework import serializers
from .models import Cart, CartItem


class CartSerializer(serializers.ModelSerializer):
    total_cost = serializers.ReadOnlyField()

    class Meta:
        model = Cart
        fields = ['id', 'total_cost']


class CartItemSerializer(serializers.ModelSerializer):
    cost = serializers.ReadOnlyField()
    price = serializers.ReadOnlyField(source="dish_size.price")

    class Meta:
        model = CartItem
        fields = [
            "id",
            "cart",
            "dish",
            "amount",
            "dough_type",
            "dish_size",
            "cost",
            "price",
        ]
