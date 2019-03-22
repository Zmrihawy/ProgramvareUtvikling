from django.urls import path
from . import views
from django.views.decorators.cache import cache_page


app_name = 'browse'
urlpatterns = [
    path('', cache_page(None)(views.browse), name='browse'),
    path('browsepage/', views.browsepage, name='browsepage'),
    path('searchresults/ingredients/', views.ing_searchresults, name='ing_searchresults'),
    path('searchresults/recipes/', views.rec_searchresults, name='rec_searchresults'),
]