from django.urls import path
from . import views

app_name = 'search'
urlpatterns = [
    path('search/', views.contribute, name='search'),
    path('results/', views.browse, name='results'),
]