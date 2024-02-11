from django.db import models
import datetime

#Categorias de produtos
class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self): 
        return self.nome
    

#Clientes
class Cliente(models.Model):
    primeiro_nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    fone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=100)

    def __str__(self): 
        return f'{self.primeiro_nome} {self.sobrenome}'


#Todos produtows
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)
    descricao = models.CharField(max_length=250, default='', blank=True, null=True)
    #imagem = models.ImageField(upload_to='uploads/produto/')
    #COISAS DE SALDÃO
    e_saldo = models.BooleanField(default = False)
    preco_saldo = models.DecimalField(default = 0, decimal_places = 2, max_digits = 6)
    

    def __str__(self): 
        return self.nome



#Todas as ordens
class Ordem(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)
    endereco = models.CharField(max_length=100, default='', blank=True)
    fone = models.CharField(max_length=20, default='', blank=True)
    data = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self): 
        return self.produto
    
    class Meta:
        verbose_name_plural = 'ordens'