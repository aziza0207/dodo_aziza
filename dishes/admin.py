from django.contrib import admin
from .models import Dish, Topping, Category, SizeType, DishSize


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


class DishAdmin(admin.ModelAdmin):
    list_display = ['category', 'title']


class SizeTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register(Dish, DishAdmin)
admin.site.register(Topping)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SizeType, SizeTypeAdmin)
admin.site.register(DishSize)
