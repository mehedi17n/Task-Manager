from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views
urlpatterns = [
    # - Home
    path('', views.home, name = ""),

    # - Register
    path('register/', views.register, name='register'),

    # - Login
    path('my-login/', views.my_login, name = "my-login"),

    # - Dashboard
    path('dashboard/', views.dashboard, name = "dashboard"),

    # - Logout
    path('user-logout/', views.user_logout, name = "user-logout"),
]
