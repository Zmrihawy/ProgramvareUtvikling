from django.urls import path
from .views import RecipeCreateView, RecipeDetailView, IngredientCreateView, ContributeCreateView
from . import views

app_name = 'recipe'
urlpatterns = [
    path('contribute/', ContributeCreateView.as_view(), name='contribute'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('add_ingredient/', IngredientCreateView.as_view(), name='add-ingredient'),
    path('add_recipe/', RecipeCreateView.as_view(), name='add-recipe')
]