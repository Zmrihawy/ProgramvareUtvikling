from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from .models import Recipe

# Create your views here.
class RecipeCreateView(CreateView):
    template_name = "recipe/contribute.html"
    model = Recipe
    fields = ['name', 'description','instruction','ingredients']

class RecipeDetailView(DetailView):
    model = Recipe