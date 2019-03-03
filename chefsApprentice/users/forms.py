from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    #CHOICES = (('1', 'Chef',), ('2', 'User',))
    #choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

