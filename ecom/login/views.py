from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms

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

def cadastro_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            #LOGANDO USUÁRIO
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Você criou sua conta com sucesso!'))
            return redirect('home')
        else:
            messages.success(request, ('Houve um erro no cadastro, verifique suas informações e tente novamente.'))
            return redirect('cadastro')
    else:
        return render(request, 'cadastro.html', {'form':form})