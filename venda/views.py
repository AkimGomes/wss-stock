# from django.shortcuts import redirect, render, get_object_or_404
# from produto.models import EstoqueProduto
# from venda.forms import ProdutoVendaForm, VendaForm
# from venda.models import Venda, ProdutoVenda
# from django.forms import formset_factory, modelformset_factory
#
#
# def criar_venda(request):
#     ProdutoVendaFormSet = formset_factory(ProdutoVendaForm, extra=1)
#
#     if request.method == 'POST':
#         venda_form = VendaForm(request.POST)
#         produto_venda_formset = ProdutoVendaFormSet(request.POST, prefix='produto')
#
#         if venda_form.is_valid() and produto_venda_formset.is_valid():
#             venda = venda_form.save()  # Save the Venda object
#
#             total_preco = 0  # Variable to store the total price
#
#             for form in produto_venda_formset:
#                 if form.cleaned_data.get('produto_vendido') and form.cleaned_data.get('quantidade'):
#                     produto_venda = form.save(commit=False)
#                     produto_venda.venda = venda
#                     produto_venda.save()
#
#                     total_preco += produto_venda.produto_vendido.preco_venda * produto_venda.quantidade
#
#                     id_produto = produto_venda.produto_vendido.id
#                     quantidade = produto_venda.quantidade
#
#                     estoque_produto = EstoqueProduto.objects.get(id_produto=id_produto)
#                     estoque_produto.quantidade -= quantidade
#                     estoque_produto.save()
#
#             venda.preco_total = total_preco
#             venda.save()
#
#             return redirect('index')
#     else:
#         venda_form = VendaForm()
#         produto_venda_formset = ProdutoVendaFormSet(prefix='produto')
#
#     return render(request, 'produto/venda_produto.html', {
#         'venda_form': venda_form,
#         'produto_venda_formset': produto_venda_formset,
#     })
#
#
# def visualizar_vendas(request):
#     vendas = Venda.objects.all()
#     return render(request, 'produto/visualizar_vendas.html', {'vendas': vendas})
#
#
# def excluir_venda(request, venda_id):
#     venda = get_object_or_404(Venda, id=venda_id)
#     venda.delete()
#     return redirect('visualizar_vendas')
#
#
# def venda_info(request, venda_id):
#     venda = get_object_or_404(Venda, id=venda_id)
#     produtos_venda = ProdutoVenda.objects.filter(venda=venda).all()
#
#     context = {
#         'venda': venda,
#         'produtos_venda': produtos_venda,
#     }
#
#     return render(request, 'produto/venda_info.html', context)
