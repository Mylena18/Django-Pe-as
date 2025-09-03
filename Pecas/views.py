from django.shortcuts import render, redirect, get_object_or_404
from .models import Fornecedor, Peca
from .forms import FornecedorForm, PecaForm

#FORNEC
def fornecedor_list(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'fornecedor_list.html', {'fornecedores': fornecedores})

def fornecedor_create(request):
    if request.method == "POST":
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fornecedor_list')
    else:
        form = FornecedorForm()
    return render(request, 'fornecedor_form.html', {'form': form})

def fornecedor_update(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    if request.method == "POST":
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            return redirect('fornecedor_list')
    else:
        form = FornecedorForm(instance=fornecedor)
    return render(request, 'fornecedor_form.html', {'form': form})

def fornecedor_delete(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    fornecedor.delete()
    return redirect('fornecedor_list')


#PECA
def peca_list(request):
    pecas = Peca.objects.all()
    return render(request, 'peca_list.html', {'pecas': pecas})

def peca_create(request):
    if request.method == "POST":
        form = PecaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('peca_list')
    else:
        form = PecaForm()
    return render(request, 'peca_form.html', {'form': form})

def peca_update(request, pk):
    peca = get_object_or_404(Peca, pk=pk)
    if request.method == "POST":
        form = PecaForm(request.POST, instance=peca)
        if form.is_valid():
            form.save()
            return redirect('peca_list')
    else:
        form = PecaForm(instance=peca)
    return render(request, 'peca_form.html', {'form': form})

def peca_delete(request, pk):
    peca = get_object_or_404(Peca, pk=pk)
    peca.delete()
    return redirect('peca_list')

