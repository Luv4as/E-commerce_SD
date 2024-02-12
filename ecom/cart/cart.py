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