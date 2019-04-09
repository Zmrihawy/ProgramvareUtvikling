from django import forms
from .models import Recipe, Ingredient


# ingredient form
class IngredientForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    info = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Ingredient
        fields = ['name', 'info']


# recipe form
class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ['name', 'description', 'instruction', 'image', 'view']
