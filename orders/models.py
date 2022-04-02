
from django.db import models
from enum import Enum
from dishes.models import Dish


class Cart(models.Model):
    date = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    DOUGH_TYPE_CHOICES = [
        ("traditional", "Традиционное"),
        ("slim", "Тонкое")]
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    dish = models.ForeignKey("dishes.Dish", on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    dough_type = models.CharField(max_length=100, choices=DOUGH_TYPE_CHOICES, null=True)
    dish_size = models.ForeignKey("dishes.DishSize", on_delete=models.SET_NULL, null=True)

