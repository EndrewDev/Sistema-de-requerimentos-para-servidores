from django.shortcuts import render, redirect, get_object_or_404
from .models import Funcao

# Create your views here.

def listas_funcao(request):
    funcao = Funcao.objects.all()
    search = request.GET.get('search')
    if search:
        funcao = funcao.filter(titulo__icontains=search)
    return render(request, 'listas-funcao.html', {'funcao': funcao})
 
def criado_funcao(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')

        if Funcao.objects.filter(titulo=titulo).exists():
            return render(request, 'criado-funcao.html', {'error': 'Já existe um função com esse título'})
    
        Funcao.objects.create(titulo=titulo, descricao=descricao)
        return redirect('listas-funcao')
    return render(request, 'criado_funcao.html')

def atualizacao_funcao(request, pk):
    funcao_atualizado = get_object_or_404(Funcao, pk=pk)

    if request.method == "POST":
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')

        if len(titulo) > 0:
            funcao_atualizado.titulo = titulo
        if len(descricao) > 0:
            funcao_atualizado.descricao = descricao
        funcao_atualizado.save()
        return redirect('listas-funcao')
    return render(request, "funcao-atualizado.html", {'funcao-atualizado': funcao_atualizado})

def deleta_funcao(request, pk):
    deleta_funcao = get_object_or_404(Funcao, pk=pk)
    deleta_funcao.delete()
    return redirect('listas-funcao')
