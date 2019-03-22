from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from recipe.models import Recipe, Ingredient
from django.contrib.auth.models import User

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

from django.views.generic import DetailView



import csv, io

from django.contrib.auth.models import Group



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            groups = form.cleaned_data.get('groups')
            for group in groups:
                user.groups.add(group)

            messages.success(request, f'Account created for {username} you can now log in')
            return redirect('users:login')


    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('users:profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    recipes = Recipe.objects.filter(user=request.user)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'recipes': recipes
    }
    return render(request, 'users/profile.html', context)


#chef_group = Group.objects.create(name = 'chef')
            #user_group = Group.objects.create(name = 'user')
#if user:
               # user1.groups.add(user_group)
            #else:
                #user1.groups.add(chef_group)

    #user = request.POST.get('user')

    return render(request, 'users/profile.html')

@login_required
def favourite(request):

    recipes = Recipe.objects.filter(favourite=request.user)
    context = {
        'recipes': recipes
    }
    return render(request, 'users/favourite.html', context)



@permission_required('admin.can_add_log_entry')
def recipe_upload(request):
    template = "users/recipe_upload.html"

    prompt = {
        'order': "Order of csv should be user, name, description, instruction, ingredients and image"
    }
    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This file is not a .csv file")

    data_set = csv_file.read().decode('utf-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    count = 0
    for column in csv.reader(io_string, delimiter=',', quotechar='"'):
        _, created = Recipe.objects.update_or_create(
            user=User.objects.get(username=column[0]),
            name=column[1],
            description=column[2],
            instruction=column[3],
        )
        count += 1
    context = {}
    messages.success(request, f'data successfully added')
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def ingredient_upload(request):
    template = "users/ingredient_upload.html"

    prompt = {
        'order': "Order of csv should be user, name and info"
    }
    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This file is not a .csv file")

    data_set = csv_file.read().decode('utf-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Ingredient.objects.update_or_create(
            user=User.objects.get(username=column[0]),
            name=column[1],
            info=column[2],
        )
    messages.success(request, f'data successfully added')
    context = {}
    return render(request, template, context)

class UserDetailView(DetailView):
    model = User
    slug_field = "username"



class UserRecDetailView(DetailView):
    model = Recipe



    def get(self, request, pk):
        recipe = self.get_object()
        recipes = Recipe.objects.filter(user=pk, view=False)
        context = {
            'recipes': recipes

        }
        return render(request, 'users/user_rec_detail.html', context)



