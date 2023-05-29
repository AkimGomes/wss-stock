from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from cliente.forms import ClienteForm
from .forms import OrcamentoForm
from .models import Orcamento, Cliente
from django.forms import modelformset_factory, modelform_factory


def visualizar_orcamentos(request):
    orcamentos = Orcamento.objects.filter(ativo_inativo=True).order_by('data_orcamento')

    context = {
        'orcamentos': orcamentos
    }

    return render(request, 'produto/visualizar_orcamentos.html', context)



def cadastrar_orcamento_cliente(request):
    if request.method == 'POST':
        orcamento_form = OrcamentoForm(request.POST)
        cliente_form = ClienteForm(request.POST, prefix='cliente')

        if orcamento_form.is_valid() and cliente_form.is_valid():
            cliente_instance = cliente_form.save()
            orcamento_instance = orcamento_form.save(commit=False)
            orcamento_instance.cliente_orcamento = cliente_instance
            orcamento_instance.save()

            return redirect('visualizar_orcamentos')

    else:
        orcamento_form = OrcamentoForm()
        cliente_form = ClienteForm(prefix='cliente')

    return render(request, 'cadastrar_orcamento_cliente.html', {
        'orcamento_form': orcamento_form,
        'cliente_form': cliente_form,
    })






