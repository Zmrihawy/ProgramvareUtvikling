from django.shortcuts import render
from django.contrib import messages
from recipe.models import Recipe, Ingredient
from django.db.models import Q


# Create your views here.

def browse(request):
    # added functionality to show all recipes in random sequence
    results = Recipe.objects.filter(Q(view=False))
    recipes_rand = list(dict.fromkeys(results))
    from random import shuffle
    shuffle(recipes_rand)
    context = {
        'recipes': recipes_rand,
    }
    return render(request, 'browse/browse.html', context)

def browsepage(request):
    results = Recipe.objects.filter(Q(view=False))
    recipes = list(dict.fromkeys(results))
    context = {
        'recipes': recipes
    }
    return render(request, 'browse/browsepage.html', context)

def searchresults(request):
    query = request.GET.get('q')
    results = Recipe.objects.filter(Q(ingredients__name__icontains=query, view=False))



    #context = {
    #    'recipes': results
    #}
    # Funksjon for å søke på det som står i søkefeltet
    results = list(dict.fromkeys(results))

    context = {
        'recipes': results,
        'ingredient': query,

    }
    return render(request, 'browse/searchresults.html', context)

def favorites(request):
    if request.method == 'POST':
        recipe = Recipe.objects.get(pk='pk')
        messages.success(request, f'liked')



