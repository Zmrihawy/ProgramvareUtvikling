from django.views.generic import CreateView, DetailView
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Recipe
from .forms import RecipeForm

# Create your views here.
class RecipeCreateView(CreateView):
    template_name = "recipe/contribute.html"
    model = Recipe
    fields = ['name', 'description','instruction','ingredients']

    def form_valid(self, form):
        form.instance.user = self.request.user #Så langt kom jeg, må fortsatt endre html så denne referer til feltene over -Torstein
        return super().form_valid(form)

    def get(self, request):
        form = RecipeForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RecipeForm(request.POST)
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

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)


class RecipeDetailView(DetailView):
    model = Recipe