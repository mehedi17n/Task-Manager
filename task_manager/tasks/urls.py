from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views
urlpatterns = [
    path('', views.home),
    #path('register/', views.register),
    path('my-login/', views.my_login),
    path('create-task/', views.createTask, name='create-task'),
    path('view-task/', views.viewTask, name='view-task'),
    path('update-task/<str:pk>/', views.updateTask, name='update-task'),
    path('delete-task/<str:pk>/', views.deleteTask, name='delete-task'),


]
