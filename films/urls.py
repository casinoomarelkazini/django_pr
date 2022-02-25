from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('films/', views.films, name="films"),
    path('film/<str:pk_test>', views.film, name="film"),
    path('film_tip/<str:pk_test>/<str:pk_user>/', views.film_tip, name="film_tip"),

    #path('user/', views.userPage, name="user"),

    path('like/', views.like_film, name='like_film'),

    path('watch_film/', views.watch_film, name='watch_film'),
    path('add_film/', views.add_film, name="add_film"),
    path('delete_film/<str:pk>', views.delete_film, name="delete_film"),

    path('tips/', views.tips, name="tips"),

    path('userPage/<str:pk_test>', views.userPage, name="userPage"),
    path('update_user/<str:pk>', views.update_user, name="update_user"),
    path('delete_user/<str:pk>', views.delete_user, name="delete_user"),

    path('table_stars_sorted', views.table_stars_sorted, name="table_stars_sorted"),
    path('table_platform_sorted', views.table_platform_sorted, name="table_platform_sorted"),
]

