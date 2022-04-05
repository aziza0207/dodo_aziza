from django.db import models

from django.db import models

from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'categories'


class Topping(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'


class Dish(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    topping = models.ManyToManyField(Topping)

    def __str__(self):
        return "{} ({})".format(self.title, self.category)

    class Meta:
        verbose_name_plural = 'dishes'
        ordering = ['category']


class SizeType(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class DishSize(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    size_type = models.ForeignKey(SizeType, on_delete=models.CASCADE)
    size_value = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    price = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.size_type} {self.dish}'
