from django import forms
from .models import Orcamento


class OrcamentoForm(forms.ModelForm):
    class Meta:
        model = Orcamento
        fields = ['nome', 'descricao', 'cliente_orcamento', 'observacao', 'data_orcamento']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'cliente_orcamento': forms.Select(attrs={'class': 'form-control'}),
            'observacao': forms.Textarea(attrs={'class': 'form-control'}),
            'data_orcamento': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }
