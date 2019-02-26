from django.urls import path
from . import views

app_name = 'browse'
urlpatterns = [
    path('contribute/', views.contribute, name='contribute'),
    path('browse/', views.browse, name='browse'),
    path('browsepage/', views.browsepage, name='browsepage'),
]