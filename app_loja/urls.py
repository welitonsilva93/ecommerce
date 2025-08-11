from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home_geral, name='home_geral'),
    path('home/<int:categoria_id>/', home, name='home'), 
    path('produto/<int:produto_id>/', detalhes_produto, name='produto'),
    path('ver_carrinho/', ver_carrinho, name='carrinho'),
    path('remover_item/<int:produto_id>/', remover_item_carrinho, name='remover_item'),
    path('finalizar_compra/', finalizar_compra, name='finalizar_compra'),
    path('finalizacao/', finalizacao, name='finalizacao'),
    path('minhas_compras/', minhas_compras, name='minhas_compras')
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
