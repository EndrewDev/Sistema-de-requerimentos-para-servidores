from django.shortcuts import render, redirect, get_list_or_404
from .models import TipoRequerimento, Processo
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

# Tipo requerimento
@login_required
def listar_tiporequerimento(request):
    tipo_requerimento = TipoRequerimento.objects.all()
    search = request.GET.get('search')

    if search: 
        tipo_requerimento = tipo_requerimento.filter(titulo_icontains=search)
    return render(request, 'tiporequerimento.html', {'requerimento': tipo_requerimento})

@login_required
def create_requerimento(request):
    if request.method == 'POST':
        titulo                  = request.POST.get('titulo')
        texto_padrao            = request.POST.get('texto_padrao')
        documentos_obrigatorios = request.POST.get('documentos_obrigatorios')
        
    

# Processo
@login_required
def listar_processo(request):
    processo = TipoRequerimento.objects.all()
    search = request.GET.get('search')

    if search: 
        processo = processo.filter(titulo_icontains=search)
    return render(request, 'processo.html', {'processo': processo})