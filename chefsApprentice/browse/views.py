from django.shortcuts import render

# Create your views here.

def browse(request):
    return render(request, 'browse/browse.html')

def browsepage(request):
    return render(request, 'browse/browsepage.html')

def contribute(request):
    return render(request, 'browse/contribute.html')