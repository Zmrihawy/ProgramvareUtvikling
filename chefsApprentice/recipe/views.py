from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from recipe.models import Recipe, Ingredient
from .forms import RecipeForm, IngredientForm
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User


# view for creating a recipe
class RecipeCreateView(CreateView):
    template_name = "recipe/add_recipe.html"
    model = Recipe
    fields = ['name', 'description', 'instruction', 'ingredients', 'image']

    # gets ingredients from the database and stores them in a dictionary
    def get(self, request):
        form = RecipeForm()
        # gets ingredient from database
        results = Ingredient.objects.values_list('name', flat=True) #Finner alle ingredienser
        results = list(dict.fromkeys(results)) #Fikser slik de kommer i en liste
        # stores recipe form and ingredient result in the dictionary
        context = {
            'form': form,
            'inglist': results #Sender denne til add_recipe templaten og brukes til autofyll
        }

        return render(request, self.template_name, context)

    # Posts the recipe and sends a request to save the recipe to the database
    def post(self, request):
        form = RecipeForm(request.POST, request.FILES or None)
        searchbar_ingredients = None
        # checks if the form is valid
        if form.is_valid():
            post = form.save(commit=False)
            # post_user checks which user is posting, only works for admins for now
            # left field for user in forms.py, so one can choose which user to post as
            # saves the form to the database
            # checks if user is logged in
            if self.request.user.is_authenticated:
                # Sets the authenticated user as the author for the recipe
                post.user = self.request.user
            else:
                # If user is not authenticated the author is default the user with username: 'Unknown'
                post.user = User.objects.get(username="Unknown")
            # saves the recipe
            post.save() #Required save so that recipe-object gets assigned an id

            #name = form.cleaned_data['name'] #This is how to fetch the info already in the form

            searchbar_ingredients = request.POST.get('added_ings').split(',') #Imports string from the "added_ings"-input in the add-recipe template, this is just a string so have to split it into list

            for ingredient_name in searchbar_ingredients:                           #Iterate through the ing-names, the list we just created from the string
                if Ingredient.objects.filter(name=ingredient_name).first() != None: #Check if ingredient in database. This is to ensure no errors on invalid ingredient input
                    post.ingredients.add(Ingredient.objects.get(name=ingredient_name))  #Look up the ingredient-objects in the database and add them to the ingredients-list of the recipe


            #Redirects to the browsepage
            return redirect('/browsepage')

        args = {'form': form}
        return render(request, self.template_name, args)


# view for viewing a recipe
class RecipeDetailView(DetailView):
    model = Recipe

    # handles permissions for user viewing the recipe
    def dispatch(self, request, *args, **kwargs):
        # user is authenticated user
        user = request.user
        # fetches the recipe for view
        recipe = self.get_object()
        # checks if recipe is private
        if recipe.view:
            # checks if user is not the author or an admin
            if not (recipe.user == user or user.is_superuser):
                # user is denied access for viewing the recipe
                raise PermissionDenied
        return super(RecipeDetailView,self).dispatch(request, *args, **kwargs)


# offline view for viewing a recipe
# difference from RecipeDetailView is that this page is cached
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


# view for updating a recipe
class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    fields = ['name', 'description', 'instruction', 'ingredients', 'image', 'view']
    template_name = 'recipe/recipe_update_form.html'

    # checks if form is valid
    def form_valid(self, form):
        form.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.user or self.request.user.is_superuser:
            return True
        return False


# view for deleting recipe
class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe

    # handles user permissions for deleting recipe
    def dispatch(self, request, *args, **kwargs):
        # fetches user
        user = request.user
        # fetches recipe
        recipe = self.get_object()
        success_url = self.get_success_url()
        # checks if user is not the author or an admin
        if not (recipe.user == user or user.is_superuser):
            raise PermissionDenied
        return super(RecipeDeleteView,self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('browse:browsepage')


# view for creating ingredients
class IngredientCreateView(CreateView):
    template_name = "recipe/add_ingredient.html"
    model = Ingredient
    fields = ['name', 'info']

    # fetches the ingredient form
    def get(self, request):
        form = IngredientForm()
        return render(request, self.template_name, {'form': form})

    # posts the ingredient and sends a request to add the ingredient to the database
    def post(self, request):
        form = IngredientForm(request.POST)
        # checks if form is valid
        if form.is_valid():
            post = form.save(commit=False)
            # checks if user is authenticated
            if self.request.user.is_authenticated:
                # sets the authenticated user as author
                post.user = self.request.user
            else:
                # sets the author as user: 'Unknown'
                post.user = User.objects.get(username="Unknown")
            # saves the ingredient
            post.save()
            # redirects to browsepage
            return redirect('/browsepage')

        args = {'form' : form}
        return render(request, self.template_name, args)


# method to add or remove a recipe from favourites
def change_favourite(request, operation, pk):
    # models Recipe model
    recipe = Recipe
    # fetches the recipe
    recipe = recipe.objects.get(pk=pk)
    # handles operations in in page view
    # adds the recipe to favourites for the authenticated user
    if operation == 'add':
        recipe.favourite.add(request.user)
    # adds the recipe to favourites for the authenticated user
    elif operation == 'remove':
        recipe.favourite.remove(request.user)
    # redirects to browsepage
    return redirect('browse:browsepage')
