from django import forms
from .models import Peca

class PecaForm(forms.ModelForm):
    class Meta:
        model = Peca
        fields = [
            'descricao', 'fornecedor', 
            'endereco_rua', 'endereco_numero', 'endereco_complemento',
            'endereco_bairro', 'endereco_cidade', 'endereco_estado', 'endereco_cep',
            'telefone_fornecedor', 'marca'
        ]
        widgets = {
            'descricao': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite a descrição da peça'
            }),
            'fornecedor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome do fornecedor'
            }),
            'endereco_rua': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome da rua'
            }),
            'endereco_numero': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número'
            }),
            'endereco_complemento': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Complemento (opcional)'
            }),
            'endereco_bairro': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Bairro'
            }),
            'endereco_cidade': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cidade'
            }),
            'endereco_estado': forms.Select(attrs={
                'class': 'form-control'
            }),
            'endereco_cep': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '00000-000'
            }),
            'telefone_fornecedor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o telefone do fornecedor'
            }),
            'marca': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite a marca da peça'
            }),
        }
        labels = {
            'descricao': 'Descrição da Peça',
            'fornecedor': 'Fornecedor',
            'endereco_rua': 'Rua',
            'endereco_numero': 'Número',
            'endereco_complemento': 'Complemento',
            'endereco_bairro': 'Bairro',
            'endereco_cidade': 'Cidade',
            'endereco_estado': 'Estado',
            'endereco_cep': 'CEP',
            'telefone_fornecedor': 'Telefone do Fornecedor',
            'marca': 'Marca da Peça',
        }