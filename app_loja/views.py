from django.shortcuts import render
from .models import *


def home(request):
    produtos = Produtos.objects.all()
    categorias = Categoria.objects.all()

    return render(request, 'app_loja/index.html', context= {'produtos': produtos, 'categorias': categorias})
