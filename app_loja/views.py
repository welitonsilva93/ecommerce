from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import AdicionarCarrinhoForm

def home(request):
    produtos = Produtos.objects.all()
    categorias = Categoria.objects.all()

    return render(request, 'app_loja/index.html', context= {'produtos': produtos, 'categorias': categorias})


def detalhes_produto(request, produto_id):
    produto = get_object_or_404(Produtos, id=produto_id)
    form = AdicionarCarrinhoForm()


    if request.method == 'POST':
        form = AdicionarCarrinhoForm(request.POST)
        if form.is_valid():
            quantidade = form.cleaned_data['quantidade']
            if quantidade > 0:
                carrinho, _ = Carrinho.objects.get_or_create(usuario=request.user)

                item, created = ItemCarrinho.objects.get_or_create(
                    carrinho = carrinho,
                    produto = produto,
                    defaults={'quantidade':quantidade}
                )
            if not created:
                item.quantidade += quantidade
                item.save()

            return redirect('ver_carrinho')
        
    context = {'produto': produto, 'form': form}
    return render(request, 'app_loja/details.html', context)