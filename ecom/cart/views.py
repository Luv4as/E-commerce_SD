from django.shortcuts import render, get_object_or_404
from .cart import Cart
from loja.models import Produto
from django.http import JsonResponse

def cart_summary(request):
    # Pega o carrinho
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_qty

    return render(request, 'cart/cart_summary.html', {"cart_products": cart_products, "quantities":quantities})

def cart_add(request):
    # Pegar o carrinho
    cart = Cart(request)
    # Testar o POST
    if request.POST.get('action') == 'post':
        # Pegar as coisas
        produto_id = int(request.POST.get('produto_id'))
        produto_qty = int(request.POST.get('produto_qty'))

        # Procurar o produto no bd
        produto = get_object_or_404(Produto, id=produto_id)

        # Salvar na sessão
        cart.add(produto=produto, quantity=produto_qty)
        
        # Qunatidade do carrinho
        cart_quantity = cart.__len__()

        # Retornar resposta
        # response = JsonResponse({'Product name: ': produto.nome})
        response = JsonResponse({'qty: ':cart_quantity})


        return response

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') =='post':
        # Pegar as coisas
        produto_id = int(request.POST.get('produto_id'))
        # Chamar a função de deletar
        cart.delete(produto=produto_id)

        # Retornar resposta
        
        response = JsonResponse({'produto':produto_id})
        return response


def cart_update(request):
    pass