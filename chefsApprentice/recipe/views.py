from django.views.generic import CreateView, DetailView
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Recipe, Ingredient
from .forms import RecipeForm, IngredientForm
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
            #post.user = request.user
            # saves the form to the database
            post.save()
            text = form.cleaned_data['name']
            form = RecipeForm()
            # redirects to the browsepage
            return redirect('/browsepage')

        args = {'form': form}
        return render(request, self.template_name, args)


class RecipeDetailView(DetailView):
    model = Recipe



#class RecipeEditView(UpdateView):
#    model = Recipe

#    template_name = "recipe/recipe_edit.html"

#    def get_object(self, *args, **kwargs):
#        recipe = get_object_or_404(Recipe, pk=self.kwargs['pk'])

#        return recipe.



class IngredientCreateView(CreateView):
    template_name = "recipe/add_ingredient.html"
    model = Ingredient
    fields = ['user', 'name', 'info']

    def get(self, request):
        form = IngredientForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = IngredientForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/browsepage')

        args = {'form' : form}
        return render(request, self.template_name, args)


class ContributeCreateView(CreateView):
    template_name = "recipe/contribute.html"

    def get(self, request):
        return render(request, self.template_name)

