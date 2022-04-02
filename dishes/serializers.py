from rest_framework import serializers
from .models import Dish, DishSize, DishTopping, SizeType, Topping, Category


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'


class DishSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishSize
        fields = '__all__'


class DishToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishTopping
        fields = '__all__'


class SizeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeType
        fields = '__all__'


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
