from django.shortcuts import render

# Create your views here.

def search(request):
    return render(request, 'search/search.html')

def results(request):
    return render(request, 'search/results.html')