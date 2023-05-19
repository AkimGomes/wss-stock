from django.shortcuts import redirect, render
from django.forms import formset_factory

from produto.models import EstoqueProduto
from venda.forms import ProdutoVendaForm, VendaForm
from venda.models import ProdutoVenda, Venda


def criar_venda(request):
    ProdutoVendaFormSet = formset_factory(ProdutoVendaForm, extra=1)

    if request.method == 'POST':
        venda_form = VendaForm(request.POST)
        produto_venda_formset = ProdutoVendaFormSet(request.POST, prefix='produto')

        if venda_form.is_valid() and produto_venda_formset.is_valid():
            venda = venda_form.save()  # Salva o objeto Venda

            total_preco = 0  # Variável para armazenar o preço total

            for form in produto_venda_formset:
                if form.has_changed():
                    produto_venda = form.save(commit=False)
                    produto_venda.venda = venda
                    produto_venda.save()  # Salva cada objeto ProdutoVenda vinculado à venda

                    total_preco += produto_venda.preco  # Adiciona o preço do ProdutoVenda ao preço total

                    # Retira a quantidade do estoque de produtos
                    id_produto = produto_venda.produto_vendido.id
                    quantidade = produto_venda.quantidade

                    estoque_produto = EstoqueProduto.objects.get(id_produto=id_produto)
                    estoque_produto.quantidade -= quantidade
                    estoque_produto.save()

            venda.preco_total = total_preco  # Define o preço total da Venda
            venda.save()  # Salva a venda com o preço total

            return redirect('index')
    else:
        venda_form = VendaForm()
        produto_venda_formset = ProdutoVendaFormSet(prefix='produto')

    return render(request, 'produto/venda_produto.html', {
        'venda_form': venda_form,
        'produto_venda_formset': produto_venda_formset,
    })
