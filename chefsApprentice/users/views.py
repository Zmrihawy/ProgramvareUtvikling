from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from recipe.models import Recipe, Ingredient
from django.contrib.auth.models import User
from .forms import UserRegisterForm
<<<<<<< HEAD

=======


import csv, io

from django.contrib.auth.models import Group



>>>>>>> 24f8a7810cb88ce74620234aa8672228bf7d40d7

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            groups = form.cleaned_data.get('groups')
            for group in groups:
                user.groups.add(group)
<<<<<<< HEAD
=======


>>>>>>> 24f8a7810cb88ce74620234aa8672228bf7d40d7
            messages.success(request, f'Account created for {username} you can now log in')
            return redirect('users:login')


    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
<<<<<<< HEAD
    return render(request, 'users/profile.html')
=======
    recipes = Recipe.objects.filter(user=request.user)
    context = {
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
    for column in csv.reader(io_string, delimiter=',', quotechar='"'):
        _, created = Recipe.objects.update_or_create(
            user=User.objects.get(username=column[0]),
            name=column[1],
            description=column[2],
            instruction=column[3],
        )

    context = {}
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

    context = {}
    return render(request, template, context)
>>>>>>> 24f8a7810cb88ce74620234aa8672228bf7d40d7
