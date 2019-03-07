from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
<<<<<<< Updated upstream
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
=======

>>>>>>> Stashed changes

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            groups = form.cleaned_data.get('groups')
            for group in groups:
                user.groups.add(group)

<<<<<<< Updated upstream
            messages.success(request, f'Your account was successfully created! You are now able to log in')
            return redirect('login')
=======
            messages.success(request, f'Account created for {username} you can now log in')
            return redirect('users:login')
>>>>>>> Stashed changes

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
<<<<<<< Updated upstream
    return render(request, 'users/profile.html')

#chef_group = Group.objects.create(name = 'chef')
            #user_group = Group.objects.create(name = 'user')
#if user:
               # user1.groups.add(user_group)
            #else:
                #user1.groups.add(chef_group)

    #user = request.POST.get('user')
=======
    return render(request, 'users/profile.html')
>>>>>>> Stashed changes
