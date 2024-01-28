from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import CreateUserForm, LoginForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required

# - Home
def home(request):
    return render(request, 'index.html')

# - Register
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form  = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("The User has been successfully registered")
        
    context = {'form':form}

    return render(request, 'register.html', context=context)

# - Login
def my_login(request):
    form = LoginForm
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,  username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
            
    context = {'form':form}
    return render(request, 'login.html', context=context)

# - Dashboard
@login_required(login_url='my-login')
def dashboard(request):
    return render(request, 'dashboard.html')

# - Logout
def user_logout(request):
    auth.logout(request)
    return redirect("")