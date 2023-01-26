from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Position(models.Model):
    name = models.CharField(max_length=255)
    salary = models.IntegerField()


class Employee(AbstractUser):
    position = models.ForeignKey(
        to=Position,
        on_delete=models.CASCADE,
        related_name="employees",
        blank=True,
        null=True
    )


class DishType(models.Model):
    name = models.CharField(max_length=255)


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    amount_of = models.FloatField()


class Dish(models.Model):
    name = models.CharField(max_length=255)
    dish_type = models.ForeignKey(
        to=DishType,
        on_delete=models.CASCADE,
        related_name="dishes"
    )
    ingredients = models.ManyToManyField(
        to=Ingredient,
        related_name="dishes"
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    recipe = models.TextField()


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    dishes = models.ManyToManyField(
        to=Dish,
        related_name="orders"
    )
    delivery = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    employee = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="orders"
    )
