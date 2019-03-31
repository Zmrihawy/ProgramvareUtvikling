
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, RedirectView, View, DetailView
from recipe.models import Recipe, Ingredient
from .forms import RecipeForm, IngredientForm
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page
from django.views.decorators.http import condition
from django.utils.decorators import available_attrs
from functools import wraps
from django.contrib import messages
import sys

# Create your views here.
# Method to only cache favourite recipes
def cache_if_favourite(timeout):

    def _decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def _wrapped_view(request, *args, **kwargs):
            if False:
                return view_func(request, *args, **kwargs)
            else:
                return cache_page(timeout)(view_func)(request, *args, **kwargs)

        return _wrapped_view

    return _decorator

class RecipeCreateView(CreateView):
    template_name = "recipe/add_recipe.html"
    model = Recipe

    fields = ['name', 'description', 'instruction', 'ingredients', 'image']



    def get(self, request):
        form = RecipeForm()

        results = Ingredient.objects.values_list('name', flat=True) #Finner alle ingredienser
        results = list(dict.fromkeys(results)) #Fikser slik de kommer i en liste
        context = {
            'form': form,
            'inglist': results #Sender denne til add_recipe templaten og brukes til autofyll
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = RecipeForm(request.POST, request.FILES or None)
        searchbar_ingredients = None
        if form.is_valid():
            post = form.save(commit=False)
            # post_user checks which user is posting, only works for admins for now
            # left field for user in forms.py, so one can choose which user to post as
            # saves the form to the database

            if self.request.user.is_authenticated:
                post.user = self.request.user
            else:
                post.user = User.objects.get(username="Unknown")
            post.save() #Required save so that recipe-object gets assigned an id

            #name = form.cleaned_data['name'] #This is how to fetch the info already in the form

            searchbar_ingredients = request.POST.get('added_ings').split(',') #Imports string from the "added_ings"-input in the add-recipe template, this is just a string so have to split it into list

            for ingredient_name in searchbar_ingredients:                           #Iterate through the ing-names, the list we just created from the string
                if Ingredient.objects.filter(name=ingredient_name).first() != None: #Check if ingredient in database. This is to ensure no errors on invalid ingredient input
                    post.ingredients.add(Ingredient.objects.get(name=ingredient_name))  #Look up the ingredient-objects in the database and add them to the ingredients-list of the recipe

            #post.save()

            #Redirects to the browsepage
            return redirect('/browsepage')

        args = {'form': form}
        return render(request, self.template_name, args)


class RecipeDetailView(DetailView):
    model = Recipe

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        recipe = self.get_object()
        if recipe.view:
            if not (recipe.user == user or user.is_superuser):
                raise PermissionDenied
        return super(RecipeDetailView,self).dispatch(request, *args, **kwargs)


class RecipeOfflineDetailView(DetailView):
    model = Recipe
    template_name = "recipe/recipe_detail_offline.html"

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        recipe = self.get_object()
        if recipe.view:
            if not (recipe.user == user or user.is_superuser):
                raise PermissionDenied
        return super(RecipeOfflineDetailView,self).dispatch(request, *args, **kwargs)



class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    fields = ['name', 'description', 'instruction', 'ingredients', 'image', 'view']
    template_name = 'recipe/recipe_update_form.html'


    def form_valid(self, form):
        form.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.user or self.request.user.is_superuser:
            return True
        return False



class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        recipe = self.get_object()
        success_url = self.get_success_url()
        if not (recipe.user == user or user.is_superuser):
            raise PermissionDenied
        return super(RecipeDeleteView,self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('browse:browsepage')




class IngredientCreateView(CreateView):
    template_name = "recipe/add_ingredient.html"
    model = Ingredient
    fields = ['name', 'info']

    def get(self, request):
        form = IngredientForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = IngredientForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if self.request.user.is_authenticated:
                post.user = self.request.user
            else:
                post.user = User.objects.get(username="Unknown")
            post.save()
            return redirect('/browsepage')

        args = {'form' : form}
        return render(request, self.template_name, args)



def change_favourite(request, operation, pk):
    recipe = Recipe
    recipe = recipe.objects.get(pk=pk)
    if operation == 'add':
        recipe.favourite.add(request.user)
    elif operation == 'remove':
        recipe.favourite.remove(request.user)
    return redirect('browse:browsepage')




