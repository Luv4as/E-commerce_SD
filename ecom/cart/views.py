from django.shortcuts import render, get_object_or_404
from .cart import Cart
from loja.models import Produto
from django.http import JsonResponse

def cart_summary(request):
    return render(request, 'cart/cart_summary.html', {})

def cart_add(request):
    # Pegar o carrinho
    cart = Cart(request)
    # Testar o POST
    if request.POST.get('action') == 'post':
        # Pegar as coisas
        produto_id = int(request.POST.get('produto_id'))

        # Procurar o produto no bd
        produto = get_object_or_404(Produto, id=produto_id)

        # Salvar na sessão
        cart.add(produto=produto)

        # Retornar resposta
        response = JsonResponse({'Product name: ': produto.nome})
        return response

def cart_delete(request):
    pass

def cart_update(request):
    pass