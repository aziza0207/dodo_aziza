

from django.contrib import admin
from . models import Dish, Topping, Category, SizeType, DishSize


admin.site.register(Dish)
admin.site.register(Topping)
admin.site.register(Category)
admin.site.register(SizeType)
admin.site.register(DishSize)
