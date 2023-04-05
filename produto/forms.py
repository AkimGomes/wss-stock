from django import forms


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
    preco_custo = forms.CharField(
        label="Preço de compra do Produto",
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: 1,99",
            }
        )
    )
    preco_venda = forms.CharField(
        label="Preço de venda do Produto",
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
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
