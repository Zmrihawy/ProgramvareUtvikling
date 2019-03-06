from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            groups = form.cleaned_data.get('groups')
            for group in groups:
                user.groups.add(group)

            messages.success(request, f'Your account was successfully created! You are now able to log in')
            return redirect('login')

    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

#chef_group = Group.objects.create(name = 'chef')
            #user_group = Group.objects.create(name = 'user')
#if user:
               # user1.groups.add(user_group)
            #else:
                #user1.groups.add(chef_group)

    #user = request.POST.get('user')