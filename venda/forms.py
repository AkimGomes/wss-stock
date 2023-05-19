from django import forms

from produto.models import Produto, EstoqueProduto
from venda.models import Venda, ProdutoVenda


class VendaForm(forms.ModelForm):

    class Meta:
        model = Venda
        fields = ['observacao', 'data', 'preco_total']

        widgets = {
            'observacao': forms.Textarea(attrs={'rows': 3, "class": "form-control"}),
            "data": forms.DateTimeInput(attrs={"class": "form-control"}),
            "preco_total": forms.NumberInput(attrs={"class": "form-control"}),
        }


class ProdutoVendaForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        produto = cleaned_data.get('produto_vendido')
        quantidade = cleaned_data.get('quantidade')

        if produto and quantidade:
            estoque_produto = EstoqueProduto.objects.get(id_produto_id=produto.id)
            if quantidade > estoque_produto.quantidade:
                raise forms.ValidationError(f'Quantidade insuficiente em estoque. Em estoque, {estoque_produto.quantidade}')

        return cleaned_data

    class Meta:
        model = ProdutoVenda
        fields = ['produto_vendido', 'quantidade', 'preco']
        widgets = {
            "produto_vendido": forms.Select(attrs={"class": "form-control"}),
            "quantidade": forms.NumberInput(attrs={"class": "form-control"}),
            "preco": forms.NumberInput(attrs={"class": "form-control"}),
        }
