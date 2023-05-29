from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from cliente.forms import ClienteForm
from .forms import OrcamentoForm
from .models import Orcamento, Cliente
from django.forms import modelformset_factory


def visualizar_orcamentos(request):
    orcamentos = Orcamento.objects.filter(ativo_inativo=True).order_by('data_orcamento')

    paginator = Paginator(orcamentos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }

    return render(request, 'produto/visualizar_orcamentos.html', context)


def cadastrar_orcamento_cliente(request):
    ClienteFormSet = modelformset_factory(Cliente, form=ClienteForm, extra=1)

    if request.method == 'POST':
        orcamento_form = OrcamentoForm(request.POST)
        cliente_formset = ClienteFormSet(request.POST, prefix='cliente')

        if orcamento_form.is_valid() and cliente_formset.is_valid():
            cliente_instances = cliente_formset.save()
            orcamento_instance = orcamento_form.save(commit=False)
            orcamento_instance.cliente_orcamento = cliente_instances[0]
            orcamento_instance.save()

            return redirect('visualizar_orcamentos')

    else:
        orcamento_form = OrcamentoForm()
        cliente_formset = ClienteFormSet(prefix='cliente')

    return render(request, 'cadastrar_orcamento_cliente.html', {
        'orcamento_form': orcamento_form,
        'cliente_formset': cliente_formset,
    })
