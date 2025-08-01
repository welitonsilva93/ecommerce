from django.contrib import admin
from .models import *

admin.site.register(Categoria)
admin.site.register(Produtos)
admin.site.register(ItemCarrinho)
admin.site.register(Carrinho)