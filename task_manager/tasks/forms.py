from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from . models import Task

# - Register
class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']

# - Login
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput)
    password = forms.CharField(widget=PasswordInput)


# - Create a task
class CreateTaskFrom(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content',]
        exclude = ['user',]