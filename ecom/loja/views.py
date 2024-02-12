from django.shortcuts import render, redirect
from .models import Produto
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    produtos = Produto.objects.all()
    return render(request, 'home.html', {'produtos':produtos})

def about(request):
    return render(request, 'sobre_nos.html', {})

def login_user(request):
    if  request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('Você está logado'))
            return redirect('home')

        else:
            messages.success(request, ('Houve um problema nos dados inseridos, tente novamente'))
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('Você deslogou da sua conta'))
    return redirect('home')