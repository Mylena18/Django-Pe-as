from django.contrib import admin
from .models import Peca

@admin.register(Peca)
class PecaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'fornecedor', 'endereco_cidade', 'endereco_estado', 'marca', 'data_cadastro')
    list_filter = ('endereco_estado', 'marca', 'data_cadastro')
    search_fields = ('descricao', 'fornecedor', 'marca')
    readonly_fields = ('data_cadastro', 'data_atualizacao')
    
    fieldsets = (
        ('Informações da Peça', {
            'fields': ('descricao', 'marca')
        }),
        ('Informações do Fornecedor', {
            'fields': ('fornecedor', 'telefone_fornecedor')
        }),
        ('Endereço do Fornecedor', {
            'fields': (
                'endereco_rua', 
                'endereco_numero', 
                'endereco_complemento',
                'endereco_bairro',
                'endereco_cidade',
                'endereco_estado',
                'endereco_cep'
            )
        }),
        ('Datas', {
            'fields': ('data_cadastro', 'data_atualizacao'),
            'classes': ('collapse',)
        }),
    )