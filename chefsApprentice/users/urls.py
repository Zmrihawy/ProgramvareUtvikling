from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


from .views import ingredient_upload, recipe_upload, favourite, UserDetailView, UserRecDetailView



app_name = 'users'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('upload_recipes/', recipe_upload, name='recipe-upload'),
    path('upload_ingredient/', ingredient_upload, name='ingredient-upload'),
    path('favourite/', favourite, name='your-favourites'),
    path('user_detail/<str:slug>', UserDetailView.as_view(template_name='users/user_detail.html'), name='user-detail'),
    path('user_rec_detail/<int:pk>', UserRecDetailView.as_view(), name='user-rec-detail'),

]