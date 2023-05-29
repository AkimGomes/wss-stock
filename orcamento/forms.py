from django import forms
from .models import Orcamento


class OrcamentoForm(forms.ModelForm):
    ativo_inativo = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    class Meta:
        model = Orcamento
        fields = ['nome', 'descricao', 'cliente_orcamento', 'observacao', 'data_orcamento', 'ativo_inativo']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'cliente_orcamento': forms.Select(attrs={'class': 'form-control'}),
            'observacao': forms.Textarea(attrs={'class': 'form-control'}),
            'data_orcamento': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'ativo_inativo': forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['ativo_inativo'].initial = self.instance.ativo_inativo
        else:
            self.fields['ativo_inativo'].initial = True
