from django.views.generic import CreateView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Recipe, Ingredient
from .forms import RecipeForm, IngredientForm
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

# Create your views here.


class RecipeCreateView(CreateView):
    template_name = "recipe/add_recipe.html"
    model = Recipe

    fields = ['name', 'description', 'instruction', 'ingredients', 'image']


    #def form_valid(self, form):
    #    form.instance.user = self.request.user #Så langt kom jeg, må fortsatt endre html så denne referer til feltene over -Torstein
    #    return super().form_valid(form)

    def get(self, request):
        form = RecipeForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RecipeForm(request.POST, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            # post_user checks which user is posting, only works for admins for now
            # left field for user in forms.py, so one can choose which user to post as
            # saves the form to the database
            if self.request.user.is_authenticated:
                post.user = self.request.user
            else:
                post.user = User.objects.get(username="Unknown")
            post.save()
            name = form.cleaned_data['name']

            ingredients = form.cleaned_data.get('ingredients')
            for ingredient in ingredients:
                post.ingredients.add(ingredient)

            # redirects to the browsepage
            return redirect('/browsepage')

        args = {'form': form}
        return render(request, self.template_name, args)


class RecipeDetailView(DetailView):
    model = Recipe



class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = ['name', 'description', 'instruction', 'ingredients', 'image']
    template_name = 'recipe/recipe_update_form.html'

    #def get_object(self, request, *args, **kwargs):
     #   recipe = super(RecipeUpdateView, self).get_object(*args, **kwargs)
      #  user = request.user
       # if not(recipe.user == self.request.user or user.is_superuser):
        #    raise PermissionDenied
        #return recipe



    def dispatch(self, request, *args, **kwargs):
        form = RecipeForm(request.POST, request.FILES or None)
        user = request.user
        recipe = self.get_object()
        success_url = self.get_success_url()
            # redirects to the browsepage
        if not (recipe.user == user or user.is_superuser):
            raise PermissionDenied
        return super(RecipeUpdateView,self).dispatch(request, *args, **kwargs)


    def get_success_url(self):
        return reverse_lazy('browse:browsepage')


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


class ContributeCreateView(CreateView):
    template_name = "recipe/contribute.html"

    def get(self, request):
        return render(request, self.template_name)

