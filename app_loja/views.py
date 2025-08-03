from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import AdicionarCarrinhoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home_geral(request):
    categorias = Categoria.objects.all()
    produtos = Produtos.objects.all().order_by('title')

    return render(request, 'app_loja/home.html', context= {'produtos': produtos, 'categorias': categorias})

def home(request, categoria_id):

    categorias = get_object_or_404(Categoria, id=categoria_id)
    produtos = Produtos.objects.filter(category=categorias)
    lista_categorias = Categoria.objects.all()

    return render(request, 'app_loja/index.html', context= {'produtos': produtos, 'categorias': categorias, 'lista_categorias': lista_categorias})



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

            return redirect('carrinho')
        
    context = {'produto': produto, 'form': form}
    return render(request, 'app_loja/details.html', context)

@login_required 
def ver_carrinho(request):
    carrinho = ItemCarrinho.objects.filter(carrinho__usuario=request.user)
    total = sum(item.produto.price * item.quantidade for item in carrinho)
    context = {'carrinho': carrinho, 'total': total}
    return render(request, 'app_loja/carrinho.html', context)

@login_required 
def remover_item_carrinho(request, produto_id):
    produto = get_object_or_404(Produtos, pk=produto_id)
    
    try:
        carrinho = Carrinho.objects.get(usuario=request.user)
    except Carrinho.DoesNotExist:
        messages.error(request, "Carrinho não encontrado.")
        return redirect('carrinho')

    try:
        item = ItemCarrinho.objects.get(carrinho=carrinho, produto=produto)
        
        if request.method == 'POST':
            item.delete()
            messages.success(request, "Item removido com sucesso.")
    except ItemCarrinho.DoesNotExist:
        messages.warning(request, "Item não estava no carrinho.")

    return redirect('carrinho')
