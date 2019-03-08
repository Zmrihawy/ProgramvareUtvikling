from django.urls import path
from .views import RecipeCreateView, RecipeDetailView, RecipeDeleteView, IngredientCreateView, ContributeCreateView
from . import views

app_name = 'recipe'
urlpatterns = [
    path('contribute/', ContributeCreateView.as_view(), name='contribute'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    #path('edit/<int:pk>', RecipeDetailView.as_view(), name='recipe-edit'),
    path('delete/<int:pk>/', RecipeDeleteView.as_view(), name='recipe-delete'),
    path('add_ingredient/', IngredientCreateView.as_view(), name='add-ingredient'),
    path('add_recipe/', RecipeCreateView.as_view(), name='add-recipe')
]