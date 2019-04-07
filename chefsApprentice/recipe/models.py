from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class Ingredient(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,

        blank=True,
    )
    name = models.CharField(
        blank=False,
        max_length=100,
    )

    info = models.TextField()


    def __str__(self):
        return self.name


class Recipe(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
    )
    name = models.CharField(
        blank=False,
        max_length=100,
    )
    description = models.TextField(
        blank=False,
    )
    instruction = models.TextField(
        blank=False,
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        blank=True
    )
    image = models.ImageField(default="default.png", upload_to='recipe_image')

    favourite = models.ManyToManyField(
        User,
        related_name='favourite',
        blank=True
    )
    view = models.BooleanField(
        blank=False,
        verbose_name="check this box to make your recipe private"
    )

    def __str__(self):
        return self.name, self.user

# Those classes aren't really needed here, since they are going to forms.py
#class IngredientForm(ModelForm):
#    class Meta:
#        model = Ingredient
#        fields = ['name', 'info']


#class RecipeForm(ModelForm):
#    class Meta:
#        model = Recipe
#        fields = ['user', 'name', 'description', 'instruction']
# Create your models here.

