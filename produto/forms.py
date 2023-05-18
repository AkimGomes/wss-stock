from django import forms

import produto
from produto.models import Produto


class CadastroProdutoForms(forms.Form):
    nome = forms.CharField(
        label="Nome do Produto",
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Bateria A765 Brilhante",
            }
        )
    )
    descricao = forms.CharField(
        label="Descrição do Produto",
        required=True,
        max_length=50,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Bateria referente ao celular unicórnio",
            }
        )
    )
    quantidade = forms.IntegerField(
        label="Quantidade do Produto",
        required=True,
        min_value=0,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: 10"
            }
        )
    )
    preco_custo = forms.FloatField(
        label="Preço de compra do Produto",
        required=False,
        max_value=100000,
        min_value=0,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "step": "0.01",
                "placeholder": "Ex.: 1,99",
            }
        )
    )
    preco_venda = forms.FloatField(
        label="Preço de venda do Produto",
        required=False,
        max_value=100000,
        min_value=0,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "step": "0.01",
                "placeholder": "Ex.: 1,99",
            }
        )
    )
    tipo_produto = forms.CharField(
        label="Tipo do Produto",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Bateria de Relógio",
            }
        )
    )
    descricao_tipo = forms.CharField(
        label="Descrição do Tipo do Produto",
        required=True,
        max_length=50,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Escreva descrição do tipo do produto",
            }
        )
    )


class AtualizarProdutoForms(forms.Form):
    nome = forms.CharField(
        label="Nome do Produto",
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )
    descricao = forms.CharField(
        label="Descrição do Produto",
        required=True,
        max_length=50,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
            }
        )
    )
    preco_custo = forms.FloatField(
        label="Preço de compra do Produto",
        required=False,
        max_value=100000,
        min_value=0,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "step": "0.01",
            }
        )
    )
    preco_venda = forms.FloatField(
        label="Preço de venda do Produto",
        required=False,
        max_value=100000,
        min_value=0,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "step": "0.01",
            }
        )
    )
    tipo_produto = forms.CharField(
        label="Tipo do Produto",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )
    descricao_tipo = forms.CharField(
        label="Descrição do Tipo do Produto",
        required=True,
        max_length=50,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
            }
        )
    )