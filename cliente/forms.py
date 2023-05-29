from .models import Cliente
from django import forms


class ClienteForm(forms.ModelForm):
    ativo_inativo = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'telefone_1', 'telefone_2', 'email', 'ativo_inativo']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone_1': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone_2': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'ativo_inativo': forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['ativo_inativo'].initial = self.instance.ativo_inativo
        else:
            self.fields['ativo_inativo'].initial = True
