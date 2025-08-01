from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import home, detalhes_produto, ver_carrinho

urlpatterns = [
    path('home/', home, name='home'), 
    path('produto/<int:produto_id>/', detalhes_produto, name='produto'),
    path('ver_carrinho/', ver_carrinho, name='carrinho')
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
