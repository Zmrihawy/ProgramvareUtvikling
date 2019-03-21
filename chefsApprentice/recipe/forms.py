from django import forms
from .models import Recipe, Ingredient


class IngredientForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    info = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Ingredient
        fields = ['name', 'info']


class RecipeForm(forms.ModelForm):
    #user = forms.ModelChoiceField(User)

    #name = forms.CharField(max_length=100)
    #description = forms.CharField(widget=forms.Textarea)
    #instruction = forms.CharField(widget=forms.Textarea)
    #ingredients = forms.ModelMultipleChoiceField(queryset=Ingredient.objects.all())
    #image = forms.ImageField()


    class Meta:
        model = Recipe
        fields = ['name', 'description', 'instruction', 'ingredients', 'image', 'view']
