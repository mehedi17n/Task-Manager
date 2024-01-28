from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import CreateUserForm, LoginForm, CreateTaskFrom

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required

from . models import Task

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
            return redirect('my-login')
        
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
    return render(request, 'profile/dashboard.html')

# - Logout
def user_logout(request):
    auth.logout(request)
    return redirect("")

# - Create a Task Page
@login_required(login_url='my-login')
def createTask(request):
    form = CreateTaskFrom()
    if request.method == "POST":
        form = CreateTaskFrom(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('view-tasks')
    
    context = {'form':form}
    return render(request, 'profile/create-task.html', context=context)

# - View Task
@login_required(login_url='my-login')
def viewTask(request):
    current_user = request.user
    task = Task.objects.all().filter(user=current_user)

    context = {'task':task}

    return render(request, 'profile/view-tasks.html', context=context)


# - Update Task
@login_required(login_url='my-login')
def updateTask(request, pk):
    task = Task.objects.get(id = pk)
    form = CreateTaskFrom(instance=task)
    if request.method == 'POST':
        form = CreateTaskFrom(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('view-tasks')
        
    context = {'form':form}
    return render(request, 'profile/update-task.html', context=context)

# - Delete Task
@login_required(login_url='my-login')
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('view-tasks')
    
    return render(request, 'profile/delete-task.html')