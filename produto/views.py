from django.contrib import messages
from django.shortcuts import render, redirect
from produto.forms import CadastroProdutoForms
from produto.models import Produto


def index(request):
    produto = Produto.objects.all()
    return render(request, "produto/index.html", {"produto": produto})


def cadastro_produto(request):
    form = CadastroProdutoForms()

    if request.method == "POST":
        form = CadastroProdutoForms(request.POST)

        if form.is_valid():

            nome = form["nome"].value()
            descricao = form["descricao"].value()
            preco_custo = form["preco_custo"].value()
            preco_venda = form["preco_venda"].value()
            tipo_produto = form["tipo_produto"].value()
            descricao_tipo = form["descricao_tipo"].value()

            if Produto.objects.filter(nome=nome).exists():
                messages.error(request, "Produto já cadastrado!")
                return redirect("cadastro_produto")

            produto = Produto(
                nome=nome,
                descricao=descricao,
                preco_custo=preco_custo,
                preco_venda=preco_venda,
                tipo_produto=tipo_produto,
                descricao_tipo=descricao_tipo,
            )
            produto.save()
            messages.success(request, "Produto salvo com sucesso!")
            return redirect("cadastro_produto")

    return render(request, "produto/cadastro_produto.html", {"form": form})
