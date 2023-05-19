from django import forms

from produto.models import Produto, EstoqueProduto
from venda.models import Venda, ProdutoVenda


class VendaForm(forms.ModelForm):
    produtos_venda = forms.ModelMultipleChoiceField(
        queryset=ProdutoVenda.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Venda
        fields = ['observacao', 'data', 'preco_total', 'produtos_venda']


        widgets = {
            'observacao': forms.Textarea(attrs={'rows': 3, "class": "form-control"}),
            "data": forms.DateTimeInput(attrs={"class": "form-control"}),
            "preco_total": forms.NumberInput(attrs={
                "class": "form-control",
                "readonly": "readonly",
            }),
        }


class ProdutoVendaForm(forms.ModelForm):
    class Meta:
        model = ProdutoVenda
        fields = '__all__'
        widgets = {

            'venda': forms.HiddenInput(),  # Campo oculto para o relacionamento com a venda
        }

    def clean(self):
        cleaned_data = super().clean()
        produto = cleaned_data.get('produto_vendido')
        quantidade = cleaned_data.get('quantidade')

        if produto and quantidade:
            estoque_produto = EstoqueProduto.objects.get(id_produto_id=produto.id)
            if quantidade > estoque_produto.quantidade:
                raise forms.ValidationError('Quantidade insuficiente em estoque.')

        preco = produto.preco_venda * quantidade
        preco = round(preco, 2)  # Arredonda para duas casas decimais
        cleaned_data['preco'] = preco

        return cleaned_data

    class Meta:
        model = ProdutoVenda
        fields = ['produto_vendido', 'quantidade', 'preco']
        widgets = {
            "produto_vendido": forms.Select(attrs={"class": "form-control"}),
            "quantidade": forms.NumberInput(attrs={"class": "form-control"}),
            "preco": forms.NumberInput(attrs={
                "class": "form-control",
                "readonly": "readonly",
            }),
        }

