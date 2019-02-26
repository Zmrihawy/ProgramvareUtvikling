from django.shortcuts import render
from django.views.generic import CreateView
from .models import Recipe


# Create your views here.
class RecipeCreateView(CreateView):
    template_name = "recipe/contribute.html"
    model = Recipe
    fields = ['name', 'description','instruction','ingredients']

    def form_valid(self, form):
        form.instance.user = self.request.user #Så langt kom jeg, må fortsatt endre html så denne referer til feltene over -Torstein
        return super().form_valid(form)