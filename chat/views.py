from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, User
from django.views import View

from .forms import CreateUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Chat, Message


def home(request):
    return render(request,'home.html')

def createUserView(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)

    else:
        form = CreateUserForm()
    return render(request, 'create_user.html', {'form': form})


def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('create_user')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def signoutView(request):
    logout(request)
    return redirect('home')


def createMessageView(request):

    if request.method == 'POST':
        return render(request, 'create_message.html')

    if request.method == 'GET':
        return render(request, 'create_message.html')
