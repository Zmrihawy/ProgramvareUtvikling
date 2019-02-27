from django.urls import path
from .views import RecipeCreateView, RecipeDetailView
from . import views

app_name = 'recipe'
urlpatterns = [
    path('contribute/', RecipeCreateView.as_view(), name='contribute'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail')
]