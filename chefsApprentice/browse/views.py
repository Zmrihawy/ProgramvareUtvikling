from django.shortcuts import render
from recipe.models import Recipe, Ingredient
from django.db.models import Q


# Create your views here.

def browse(request):
    return render(request, 'browse/browse.html')

def browsepage(request):
    context = {
        'recipes': Recipe.objects.all()
    }
    return render(request, 'browse/browsepage.html', context)

def searchresults(request):
    query = request.GET.get('q')
    results = Recipe.objects.filter(Q(ingredients__name__icontains=query))

    context = {
        'recipes': results
    }
    return render(request, 'browse/searchresults.html', context)


