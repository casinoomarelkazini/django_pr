from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import *

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'category', 'description', 'year','piattaforma', 'film_pic']

class TipForm(ModelForm):
    class Meta:
        model = Tip
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UpdateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']

