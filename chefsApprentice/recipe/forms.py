from django import forms
from .models import Recipe

class IngredientForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    info = forms.CharField(widget=forms.Textarea)


class RecipeForm(forms.ModelForm):
    #user = forms.ModelChoiceField(User)
    #name = forms.CharField(max_length=100)
    #description = forms.CharField(widget=forms.Textarea)
    #instruction = forms.CharField(widget=forms.Textarea)
    #ingredients = forms.ModelMultipleChoiceField(Ingredient)
    image = forms.ImageField()

    class Meta:
        model = Recipe
        fields = ['user', 'name', 'description', 'instruction', 'ingredients', 'image']
