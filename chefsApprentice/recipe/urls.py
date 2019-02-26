from django.urls import path
from .views import RecipeCreateView
from . import views

app_name = 'recipe'
urlpatterns = [
    path('contribute/', RecipeCreateView.as_view(), name='contribute'),
]