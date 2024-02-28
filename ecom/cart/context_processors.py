from .cart import Cart

# Criar processador de contexto para o carrinho funcionar em todas as páginas
def cart(request):
    # Retornar os dados padrão do carrinho
    return {'cart': Cart(request)}