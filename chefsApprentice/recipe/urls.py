from django.urls import path
from .views import RecipeCreateView, RecipeDetailView, RecipeUpdateView, RecipeDeleteView, IngredientCreateView, ContributeCreateView
from . import views
from django.conf.urls import url

app_name = 'recipe'
urlpatterns = [
    path('contribute/', ContributeCreateView.as_view(), name='contribute'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('update/<int:pk>', RecipeUpdateView.as_view(), name='recipe-update'),
    path('delete/<int:pk>/', RecipeDeleteView.as_view(), name='recipe-delete'),
    path('add_ingredient/', IngredientCreateView.as_view(), name='add-ingredient'),
    path('add_recipe/', RecipeCreateView.as_view(), name='add-recipe'),
    #path('like/<int:pk>', RecipeLikeToggle.as_view(), name='like-toggle'),
    #path('<slug:slug>/like/', RecipeLikeAPIToggle.as_view(), name='like-api-toggle'),
    url(r'^recipe/(?P<pk>\d+)/(?P<operation>.+)/$', views.change_favourite, name='change_favourite')

]