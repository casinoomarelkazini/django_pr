from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import *
from .forms import *
from .filters import *
from .decorators import *

# Create your views here.

@unathenticated_user
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                group = Group.objects.get(name='user')
                user.groups.add(group)
                
                messages.success(request, 'Account was created successfully for ' + username)
                return redirect('login')

        context = {'form':form}
        return render(request, 'accounts/register.html', context)

@unathenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect!')

    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
#################################################################################################################

@login_required(login_url='login')
@admin_only
def home(request):
    films = Film.objects.all()
    users = User.objects.all()

    myFilter = UserFilter(request.GET, queryset=users)
    users = myFilter.qs


    context = {'films':films, 'users': users, 'myFilter' : myFilter} 

    return render(request, 'accounts/dashboard.html', context)

def films(request):
    user = request.user

    films = Film.objects.all()

    myFilter = FilmFilter(request.GET, queryset=films)
    films = myFilter.qs

    context = {'films': films, 'myFilter':myFilter, 'user':user}

    return render(request, 'accounts/films.html', context)

def film_tip(request, pk_test, pk_user):
    tips = Tip.objects.all()
    user = User.objects.get(id=pk_user)
    film = Film.objects.get(id=pk_test)

    form = TipForm()

    if request.method == 'POST' :
        form = TipForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('tips')

    return render(request, 'accounts/film_tip.html', {'film':film, 'user':user, 'form':form, 'tips':tips})

def film(request, pk_test):
    film = Film.objects.get(id=pk_test)
    return render(request, 'accounts/film.html', {'film':film})

@login_required(login_url='login')
def userPage(request, pk_test):
    user = User.objects.get(id=pk_test)

    likes = Like.objects.filter(id=pk_test)
    seens = Seen.objects.filter(user_id=pk_test)

    
    list_films_seen = user.seen_set.all().filter(value=True)

    films_liked = Like.objects.filter(user_id=pk_test, value=True).count()

    films_seen = Seen.objects.filter(user_id=pk_test, value=True).count()
    
    films = Film.objects.all()


    context = {'user':user, 'films_liked':films_liked, 'films_seen':films_seen, 'seens':seens, 'films':films, 'likes':likes, 'list_films_seen': list_films_seen}
    return render(request, 'accounts/userPage.html', context)

##############################################################################################################################################

@login_required(login_url='login')
def update_user(request, pk):
    user = User.objects.get(id=pk)
    form = UpdateUserForm(instance=user)

    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return redirect('films')

    context = {'form':form}
    return render(request, 'accounts/update_user.html', context)

@login_required(login_url='login')
def delete_user(request, pk):
    user = User.objects.get(id=pk)

    if request.method == 'POST':
        user.delete()
        return redirect('/')

    context = {'user': user}
    return render(request, 'accounts/delete_user.html', context)

########################################################################################################################################

@login_required(login_url='login')
def like_film(request):
    user = request.user
    if request.method == 'POST':
        film_id = request.POST.get('film_id')
        film_obj = Film.objects.get(id = film_id)

        if user in film_obj.liked.all():
            film_obj.liked.remove(user)
        else: 
            film_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user = user, film_id = film_id)

        if not created:
            if like.value == True:
                like.value = False
            else:
                like.value = True
        like.save()

    return redirect('films')

def delete_film(request, pk):
    film = Film.objects.get(id=pk)

    if request.method == 'POST':
        film.delete()
        return redirect('/')

    context = {'film': film}
    return render(request, 'accounts/delete_film.html', context)

@login_required(login_url='login')
def watch_film(request):
    user = request.user
    if request.method == 'POST':
        film_id = request.POST.get('film_id')
        film_obj = Film.objects.get(id = film_id)

        if user in film_obj.watch.all():
            film_obj.watch.remove(user)
        else: 
            film_obj.watch.add(user)

        seen, created = Seen.objects.get_or_create(user = user, film_id = film_id)

        if not created:
            if seen.value == True:
                seen.value = False
            else:
                seen.value = True
        seen.save()

    return redirect('films')

@login_required(login_url='login')
def add_film(request):
    form = FilmForm()

    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/film_form.html', context)

#############################################################################################################################################

@login_required(login_url='login')
def make_tip(request):
    form = TipForm()

    if request.method == 'POST':
        form = TipForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('tips')

    context = {'form':form}
    return render(request, 'accounts/tip_form.html', context)


def tips(request):
    user = request.user
    tips = Tip.objects.all()
    myFilter = TipFilter(request.GET, queryset=tips)
    tips = myFilter.qs
    context = {'tips': tips, 'user':user, 'myFilter':myFilter}
    return render(request, 'accounts/tips.html', context)

def table_stars_sorted(request):
    tips = Tip.objects.all()
    tips = Tip.objects.order_by('stars').reverse()
    myFilter = TipFilter(request.GET, queryset=tips)
    tips = myFilter.qs
    context = {'tips':tips, 'myFilter':myFilter}
    return render(request, 'accounts/table_stars_sorted.html', context)

def table_platform_sorted(request):
    tips = Tip.objects.all()
    tips = Tip.objects.order_by('film__piattaforma')
    myFilter = TipFilter(request.GET, queryset=tips)
    tips = myFilter.qs
    context = {'tips':tips, 'myFilter':myFilter}
    return render(request, 'accounts/table_platform_sorted.html', context)


