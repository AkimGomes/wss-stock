from django import forms

import produto
from produto.models import Produto, EstoqueProduto


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
        ),
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
        ),
    )
    quantidade = forms.IntegerField(
        label="Quantidade do Produto",
        required=True,
        min_value=0,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Ex.: 10"}
        ),
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
        ),
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
        ),
    )
    tipo_produto = forms.CharField(
        label="Tipo do Produto",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Bateria de Relógio",
            }
        ),
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
        ),
    )


class AtualizarProdutoForms(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            "nome",
            "descricao",
            "preco_custo",
            "preco_venda",
            "tipo_produto",
            "descricao_tipo",
        ]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "descricao": forms.Textarea(attrs={"class": "form-control"}),
            "preco_custo": forms.NumberInput(
                attrs={"class": "form-control", "step": "0.01"}
            ),
            "preco_venda": forms.NumberInput(
                attrs={"class": "form-control", "step": "0.01"}
            ),
            "tipo_produto": forms.TextInput(attrs={"class": "form-control"}),
            "descricao_tipo": forms.Textarea(attrs={"class": "form-control"}),
        }

    quantidade = forms.IntegerField(
        label="Quantidade",
        required=True,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            estoque_produto = EstoqueProduto.objects.get(id_produto=self.instance.pk)
            self.fields["quantidade"].initial = estoque_produto.quantidade

    def save(self, commit=True):
        instance = super().save(commit=False)
        quantidade = self.cleaned_data["quantidade"]
        if instance.pk:
            estoque_produto = EstoqueProduto.objects.get(id_produto=instance.pk)
            estoque_produto.quantidade = quantidade
            estoque_produto.save()
        else:
            instance.save()
            EstoqueProduto.objects.create(id_produto=instance.pk, quantidade=quantidade)
        return instance
