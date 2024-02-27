from django.shortcuts import render, redirect
from .models import Produto, Categoria
from django.contrib import messages

def categoria(request, foo):
    #Troca hifen por espaço
    foo = foo.replace('-', ' ')

    #Pega categoria pela url
    try:
        # Procurar a categoria
        categoria = Categoria.objects.get(nome=foo)
        produtos = Produto.objects.filter(categoria=categoria)
        return render(request, 'categoria.html', {'produtos':produtos, 'categoria':categoria})
    except:
        messages.success(request, ('Essa categoria não existe'))
        return redirect('home')

def produto(request, pk):
    produto = Produto.objects.get(id=pk)
    return render(request, 'produto.html', {'produto':produto})

def home(request):
    produtos = Produto.objects.all()
    return render(request, 'home.html', {'produtos':produtos})

def about(request):
    return render(request, 'sobre_nos.html', {})