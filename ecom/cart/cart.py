from loja.models import Produto


class Cart():
    def __init__(self, request):
        self.session = request.session

        # Pegar a chave da sessão atual se ela existir
        cart = self.session.get('session_key')

        # Se o usuário for novo não terá chave
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        
        # Ter certeza que o carrinho é disponivel para todas páginas
        self.cart = cart

    def add(self, produto, quantity):
        produto_id = str(produto.id) # type: ignore
        produto_qty = str(quantity)

        if produto_id in self.cart:
            pass
        else:
            #self.cart[produto_id] = {'preco': str(produto.preco)}
            self.cart[produto_id] = int(produto_qty)

        self.session.modified = True

    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        # Pega ids do carrinho
        product_ids = self.cart.keys()

        # Usa ids para procurar produtos
        produtos = Produto.objects.filter(id__in=product_ids)
        return produtos
    
    def get_qty(self):
        quantities = self.cart
        return quantities