from django import forms
from .models import Fornecedor, Peca

class FornecedorForm(forms.ModelForm):
    class Meta:
        model= Fornecedor
        fields= ['nome', 'endereco', 'telefone']

class PecaForm(forms.ModelForm):
    class Meta:
        model= Peca
        fields= ['descricao', 'marca', 'fornecedor']
