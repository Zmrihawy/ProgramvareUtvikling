from django.shortcuts import render
from django.contrib import messages
from recipe.models import Recipe, Ingredient
from django.db.models import Q
from django.shortcuts import redirect


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


def ing_searchresults(request):
    search_ings = request.GET.get('added_ings').split(',')  #Get the added ingredients from the html (through the URL-bar)

    if search_ings[0] == '':                                #If we have not added any ingredients
        search_ings = [request.GET.get('search_field'),]    #Get the value in the search-field

    results = Recipe.objects.filter(Q(ingredients__name__icontains=search_ings[0], view=False)) #Init filtering
    for ing in search_ings:
        results = results.filter(Q(ingredients__name__icontains=ing))               #Loop through the ings and filter them


    results = list(dict.fromkeys(results))      #Pass the results to the ing_searchresults.html
    search_ings_str = ",".join(search_ings)

    context = {
        'recipes': results,
        'ingredient': search_ings_str,
    }
    return render(request, 'browse/ing_searchresults.html', context)


def rec_searchresults(request):
    recipe_name = request.GET.get('q')

    if recipe_name == '':
        return redirect('/browsepage/')

    results = Recipe.objects.filter(Q(name__icontains=recipe_name, view=False))

    results = list(dict.fromkeys(results))

    context = {
        'recipes': results,
        'recipe_name': recipe_name,
    }
    return render(request, 'browse/rec_searchresults.html', context)


def favorites(request):
    if request.method == 'POST':
        recipe = Recipe.objects.get(pk='pk')
        messages.success(request, f'liked')