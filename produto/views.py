from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from produto.forms import CadastroProdutoForms, AtualizarProdutoForms
from produto.models import Produto, EstoqueProduto


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
    estoque_produto = EstoqueProduto.objects.get(id_produto=produto.id)

    form = AtualizarProdutoForms(instance=produto)

    if request.method == "POST":
        form = AtualizarProdutoForms(request.POST, instance=produto)

        if form.is_valid():
            form.save()

            quantidade = form.cleaned_data.get("quantidade")
            if quantidade is not None and quantidade != estoque_produto.quantidade:
                estoque_produto.quantidade = quantidade
                estoque_produto.save()

            messages.success(request, "Produto atualizado com sucesso!")
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
            quantidade = form["quantidade"].value()

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
            estoque_produto = EstoqueProduto(
                id_produto=produto,
                quantidade=quantidade
            )
            estoque_produto.save()
            messages.success(request, "Produto salvo com sucesso!")
            return redirect("index")

    return render(request, "produto/cadastro_produto.html", {"form": form})
