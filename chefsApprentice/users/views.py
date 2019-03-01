from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django. contrib.auth.models import Group

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user1 = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')

            chef_group = Group.objects.create(name = 'chef')
            user_group = Group.objects.create(name = 'user')
            user = request.POST.get('user')
            if user:
                user1.groups.add(user_group)
            else:
                user1.groups.add(chef_group)
        return redirect('/browse')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})



