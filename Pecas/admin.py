from django.contrib import admin
from .models import Fornecedor, Peca

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display= ('nome','endereco','telefone')
    search_fields= ('nome','telefone')
    list_per_page= 10

@admin.register(Peca)
class PecaAdmin(admin.ModelAdmin):
    list_display =('descricao','marca','fornecedor')
    search_fields =('descricao','marca')
    list_filter =('marca','fornecedor')
    list_per_page= 10

