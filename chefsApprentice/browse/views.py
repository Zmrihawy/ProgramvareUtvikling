from django.shortcuts import render
from recipe.models import Recipe, Ingredient
from django.db.models import Q


# Create your views here.

def browse(request):
    # added functionality to show all recipes in random sequence
    recipes_rand = list(Recipe.objects.all())
    from random import shuffle
    shuffle(recipes_rand)
    context = {
        'recipes': recipes_rand,
    }
    return render(request, 'browse/browse.html', context)

def browsepage(request):
    context = {
        'recipes': Recipe.objects.all()
    }
    return render(request, 'browse/browsepage.html', context)

def searchresults(request):
    query = request.GET.get('q')
    results = Recipe.objects.filter(Q(ingredients__name__icontains=query))


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


