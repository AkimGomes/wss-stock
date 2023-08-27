# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib import messages
# from cliente.forms import ClienteForm
# from .forms import OrcamentoForm
# from .models import Orcamento
#
#
# def visualizar_orcamentos(request):
#     orcamentos = Orcamento.objects.filter(ativo_inativo=True).order_by('data_orcamento')
#
#     context = {
#         'orcamentos': orcamentos
#     }
#
#     return render(request, 'produto/visualizar_orcamentos.html', context)
#
#
# def cadastrar_orcamento_cliente(request):
#     if request.method == 'POST':
#         orcamento_form = OrcamentoForm(request.POST)
#         cliente_form = ClienteForm(request.POST, prefix='cliente')
#
#         if orcamento_form.is_valid() and cliente_form.is_valid():
#             orcamento_instance = orcamento_form.save(commit=False)
#             cliente_instance = cliente_form.save()
#             orcamento_instance.cliente_orcamento = cliente_instance
#             orcamento_instance.save()
#
#             messages.success(request, 'Orçamento e Cliente cadastrados com sucesso!')
#             return redirect('visualizar_orcamentos')
#         else:
#             messages.error(request, 'Preencha corretamente todos os campos.')
#
#     else:
#         orcamento_form = OrcamentoForm()
#         cliente_form = ClienteForm(prefix='cliente')
#
#     return render(request, 'cadastrar_orcamento_cliente.html', {
#         'orcamento_form': orcamento_form,
#         'cliente_form': cliente_form,
#     })
#
#
# def deletar_orcamento(request, id):
#     orcamento = get_object_or_404(Orcamento, pk=id)
#     orcamento.delete()
#     messages.success(request, "Orçamento excluído com sucesso!")
#
#     return redirect("visualizar_orcamentos")
#
#
# def orcamento_info(request, orcamento_id):
#     orcamento = get_object_or_404(Orcamento, id=orcamento_id)
#
#     context = {
#         "orcamento": orcamento,
#     }
#
#     return render(request, "produto/orcamento_info.html", context)
#
#
# def atualizar_orcamento(request, id):
#     orcamento = get_object_or_404(Orcamento, id=id)
#
#     if request.method == 'POST':
#         orcamento_form = OrcamentoForm(request.POST, instance=orcamento)
#         if orcamento_form.is_valid():
#             orcamento_form.save()
#             return redirect('visualizar_orcamentos')
#     else:
#         orcamento_form = OrcamentoForm(instance=orcamento)
#
#     return render(request, 'produto/atualizar_orcamento.html', {
#         'orcamento_form': orcamento_form,
#     })
