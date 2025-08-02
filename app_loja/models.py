from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    title = models.CharField(max_length=20)


    def __str__(self):
        return self.title

class Produtos(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=600)
    price = models.FloatField()
    category = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return self.title
    
class Carrinho(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    
    def remover(self, produto):
        try:
            item_carrinho = self.itens.get(produto=produto)
            item_carrinho.delete()
        except ItemCarrinho.DoesNotExist:
            pass
            
class ItemCarrinho(models.Model):
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name='itens')

    def __str__(self):
        return f"{self.quantidade}x {self.produto.title}"

