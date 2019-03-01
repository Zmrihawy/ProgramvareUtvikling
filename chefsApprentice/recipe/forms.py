from django import forms
from .models import Recipe, Ingredient


class IngredientForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    info = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Ingredient
        fields = ['user', 'name', 'info']


class RecipeForm(forms.ModelForm):
    #user = forms.ModelChoiceField(User)
<<<<<<< HEAD
    #name = forms.CharField(max_length=100)
    #description = forms.CharField(widget=forms.Textarea)
    #instruction = forms.CharField(widget=forms.Textarea)
    #ingredients = forms.ModelMultipleChoiceField(Ingredient)
    image = forms.ImageField()
=======
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    instruction = forms.CharField(widget=forms.Textarea)
    ingredients = forms.ModelMultipleChoiceField(queryset=Ingredient.objects.all())
    #image = forms.ImageField()
>>>>>>> a0b1536a707065c1474366c97b2b5895af7acc22

    class Meta:
        model = Recipe
        fields = ['user', 'name', 'description', 'instruction', 'ingredients', 'image']
