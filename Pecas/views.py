from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Peca
from .forms import PecaForm

def lista_pecas(request):
    pecas = Peca.objects.all()
    return render(request, 'pecas/lista_pecas.html', {'pecas': pecas})

def criar_peca(request):
    if request.method == 'POST':
        form = PecaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Peça cadastrada com sucesso!')
            return redirect('lista_pecas')
    else:
        form = PecaForm()
    
    return render(request, 'pecas/form_peca.html', {'form': form, 'titulo': 'Nova Peça'})

def editar_peca(request, id):
    peca = get_object_or_404(Peca, id=id)
    
    if request.method == 'POST':
        form = PecaForm(request.POST, instance=peca)
        if form.is_valid():
            form.save()
            messages.success(request, 'Peça atualizada com sucesso!')
            return redirect('lista_pecas')
    else:
        form = PecaForm(instance=peca)
    
    return render(request, 'pecas/form_peca.html', {'form': form, 'titulo': 'Editar Peça'})

def visualizar_peca(request, id):
    peca = get_object_or_404(Peca, id=id)
    return render(request, 'pecas/visualizar_peca.html', {'peca': peca})

def deletar_peca(request, id):
    peca = get_object_or_404(Peca, id=id)
    
    if request.method == 'POST':
        peca.delete()
        messages.success(request, 'Peça excluída com sucesso!')
        return redirect('lista_pecas')
    
    return render(request, 'pecas/confirmar_exclusao.html', {'peca': peca})