from django.db import models
from django.contrib.auth.models import User


class Ingredient(models.Model):
    name = models.CharField(
        blank=False,
        max_length=100,
    )

    info = models.TextField(
        blank=False,
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,

        blank=True,
    )

    def __str__(self):
        return self.name


class Recipe(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='authored_posts',
        blank=True,
    )
    name = models.CharField(
        blank=False,
        max_length=100,
    )
    description = models.TextField(
        blank=False,
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name='posts',
        blank=True
    )

    def __str__(self):
        return self.name
# Create your models here.
