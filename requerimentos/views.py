from django.shortcuts import render, redirect, get_object_or_404
from .models import TipoRequerimento, Processo
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

# Tipo requerimento
@login_required
def listas_tiporequerimento(request):
    tipo_requerimento = TipoRequerimento.objects.all()
    search = request.GET.get('search')

    if search: 
        tipo_requerimento = tipo_requerimento.filter(titulo_icontains=search)

    return render(request, 'lista_requerimento.html', {'requerimento': tipo_requerimento})

# Criar requerimento
@login_required
def create_requerimento(request):
    if request.method == 'POST':
        titulo                  = request.POST.get('titulo')
        texto_padrao            = request.POST.get('texto_padrao')
        documentos_obrigatorios = request.POST.get('documentos_obrigatorios')

        requerimento = requerimento (
            titulo=titulo,
            texto_padrao=texto_padrao,
            documentos_obrigatorios=documentos_obrigatorios,
        )
        requerimento.save()

        messages.success(request, "Requerimento criado com sucesso")
    
        return redirect('tiporequerimento')

    return render(request, 'criado_requerimento.html')

# Atualizar requerimento
@login_required
def atualizar_requerimento(request, pk):
    requerimento = get_object_or_404(TipoRequerimento, pk=pk)

    if request.method == 'POST':
        titulo                  = request.POST.get('titulo')
        texto_padrao            = request.POST.get('texto_padrao')
        documentos_obrigatorios = request.POST.get('documentos_obrigatorios')

        if len(titulo) > 0:
            requerimento.titulo = titulo
        if len(texto_padrao) > 0:
            requerimento.texto_padrao = texto_padrao
        if len(documentos_obrigatorios) > 0:
            requerimento.documentos_obrigatorios = documentos_obrigatorios

        requerimento.save()

        messages.success(request, 'Requerimento atualizado com sucesso')

        return redirect('tiporequerimento')
    
    return render(request, 'atualizar_requerimento.html')

# Deleta requerimento
@login_required
def delete_requerimento(request, pk):
    requerimento = get_object_or_404(TipoRequerimento, pk=pk)
    requerimento.delete()
    messages.success(request, 'Requerimento excluído com sucesso')
    return redirect('tiporequerimento')
    

# Processo
@login_required
def listas_processo(request):
    processo = TipoRequerimento.objects.all()
    search = request.GET.get('search')

    if search: 
        processo = processo.filter(titulo_icontains=search)

    return render(request, 'listas_processo.html', {'processo': processo})

# Criado processo
@login_required
def criado_processo(request):
    if request.method == "POST":
        servidor       = request.POST.get('servidor')
        tipo           = request.POST.get('tipo')
        documentos     = request.POST.get('documentos')
        info_complater = request.POST.get('info_complater')
        status         = request.POST.get('status')
        criado_em      = request.POST.get('criado_em')
        atualizado_em  = request.POST.get('atualizado_em')
        bloquaedo       = request.POST.get('bloqueado')

        processo = processo (
            servidor=servidor,
            tipo=tipo,
            documentos=documentos,
            info_complater=info_complater,
            status=status,
            criado_em=criado_em,
            atualizado_em=atualizado_em,
            bloquaedo=bloquaedo,
        )
        processo.save()

        messages.success(request, "Processo criado com sucesso")

        return redirect('processo')
    
    return render(request, 'criado_processo.html')

# Atualizar processo
@login_required
def atualizar_processo(request, pk):
    processo = get_object_or_404(Processo, pk=pk)

    if request.method == "POST":
        servidor       = request.POST.get('servidor')
        tipo           = request.POST.get('tipo')
        documentos     = request.POST.get('documentos')
        info_complater = request.POST.get('info_complater')
        status         = request.POST.get('status')
        criado_em      = request.POST.get('criado_em')
        atualizado_em  = request.POST.get('atualizado_em')
        bloquaedo       = request.POST.get('bloqueado')

        if len(servidor) > 0:
            processo.servidor = servidor
        if len(tipo) > 0:
            processo.tipo = tipo
        if len(documentos) > 0:
            processo.documentos = documentos
        if len(info_complater) > 0:
            processo.info_complementar = info_complater
        if len(status) > 0:
            processo.status = status
        if len(criado_em) > 0:
            processo.criado_em = criado_em
        if len(atualizado_em) > 0:
            processo.atualizado_em = atualizado_em
        if len(bloquaedo) > 0:
            processo.bloqueado = bloquaedo
        processo.save()

        messages.success(request, 'Processo atualizado com sucesso')

        return redirect('processo')
    
    return render(request, 'atualizado_processo')

@login_required
def delete_processo(request, pk):
    processo = get_object_or_404(Processo, pk=pk)

    if processo.bloqueado or processo.status != "pendente":
        messages.error(request, 'Este processo não pode ser excluído')
        return redirect('processo')
    
    if request.method == 'POST':
        processo.delete()
        messages.success(request, 'Processo excluído com sucesso')
        return redirect('processo')
    
    return redirect('processo')
