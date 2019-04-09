from django.urls import path
from .views import RecipeCreateView, RecipeDetailView, RecipeUpdateView, RecipeDeleteView, IngredientCreateView,\
    RecipeOfflineDetailView
from . import views
from django.conf.urls import url
from django.views.decorators.cache import cache_page


app_name = 'recipe'
urlpatterns = [
    path('recipe/<int:pk>/', (RecipeDetailView.as_view()), name='recipe-detail'),
    path('recipe_offline/<int:pk>/', cache_page(None)(RecipeOfflineDetailView.as_view()), name='recipe-offline'),
    #path('contribute/', ContributeCreateView.as_view(), name='contribute'),
    path('update/<int:pk>', RecipeUpdateView.as_view(success_url='/browsepage/'), name='recipe-update'),
    path('delete/<int:pk>/', RecipeDeleteView.as_view(), name='recipe-delete'),
    path('add_ingredient/', IngredientCreateView.as_view(), name='add-ingredient'),
    path('add_recipe/', RecipeCreateView.as_view(), name='add-recipe'),
    url(r'^recipe/(?P<pk>\d+)/(?P<operation>.+)/$', views.change_favourite, name='change_favourite'),


]