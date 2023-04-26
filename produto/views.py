from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from produto.forms import CadastroProdutoForms, AtualizarProdutoForms
from produto.models import Produto


def index(request):
    produtos_lista = Produto.objects.all()
    page = request.GET.get("page", 1)

    paginator = Paginator(produtos_lista, 10)

    try:
        produtos = paginator.page(page)
    except PageNotAnInteger:
        produtos = paginator.page(1)
    except EmptyPage:
        produtos = paginator.page(paginator.num_pages)

    return render(request, "produto/index.html", {"produtos": produtos})


def buscar(request):
    produtos = Produto.objects.filter(publicado=True)

    if "buscar" in request.GET:
        nome = request.GET.get("buscar")
        if nome:
            produtos = produtos.filter(nome__icontains=nome)

            if not produtos:
                messages.error(request, "Nenhum produto encontrado!")
                return redirect("index")

    return render(request, "produto/buscar.html", {"produtos": produtos})


def atualizar_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)

    form = AtualizarProdutoForms(
        initial={
            "nome": produto.nome,
            "descricao": produto.descricao,
            "preco_custo": produto.preco_custo,
            "preco_venda": produto.preco_venda,
            "tipo_produto": produto.tipo_produto,
            "descricao_tipo": produto.descricao_tipo,
        }
    )

    if request.method == "POST":
        form = AtualizarProdutoForms(request.POST)

        if form.is_valid():

            nome = form["nome"].value()
            descricao = form["descricao"].value()
            preco_custo = form["preco_custo"].value()
            preco_venda = form["preco_venda"].value()
            tipo_produto = form["tipo_produto"].value()
            descricao_tipo = form["descricao_tipo"].value()

            if nome != produto.nome:
                produto.nome = nome
            if descricao != produto.descricao:
                produto.descricao = descricao
            if preco_custo != produto.preco_custo:
                produto.preco_custo = preco_custo
            if preco_venda != produto.preco_venda:
                produto.preco_venda = preco_venda
            if tipo_produto != produto.tipo_produto:
                produto.tipo_produto = tipo_produto
            if descricao_tipo != produto.descricao_tipo:
                produto.descricao_tipo = descricao_tipo
            produto.save()
            messages.success(request, "Produto salvo com sucesso!")
            return redirect("index")

    return render(request, "produto/atualizar_produto.html", {"form": form})


def deletar_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    produto.delete()
    messages.success(request, "Produto excluido com sucesso!")

    return redirect("index")


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
            return redirect("index")

    return render(request, "produto/cadastro_produto.html", {"form": form})
