import django_filters
from django_filters import DateFilter
from .models import *

class FilmFilter(django_filters.FilterSet): 
    class Meta:
        model = Film
        fields = ['title', 'category','year','piattaforma']

class UserFilter(django_filters.FilterSet): 
    class Meta:
        model = User
        fields = ['username', 'email', 'is_active', 'is_staff']

class TipFilter(django_filters.FilterSet): 
    class Meta:
        model = Tip
        fields = {'stars','user__username','film__title', 'film__piattaforma'}

        
