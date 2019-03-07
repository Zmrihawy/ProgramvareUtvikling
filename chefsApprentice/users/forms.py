from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    #CHOICES = (('chef', 'Chef',), ('user', 'User',))
    #choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    #my_group = Group.objects.get(name='my_group_name')
    #my_group.user_set.add(your_user)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'groups']
