from django.shortcuts import render, redirect
from .models import Usuario, TipoUsuario, Funcao, Setor, TipoProtocolo, Protocolo
# from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.

def create_user(request):
    if request.method == "POST":
        matricula      = request.POST.get('matricula')
        rg             = request.POST.get('rg')
        cpf            = request.POST.get("cpf")
        rua            = request.POST.get("rua")   
        numero_endereco = request.POST.get("numero_endereco")
        bairro         = request.POST.get('bairro')
        cep            = request.POST.get('cep')
        numero_contato = request.POST.get("numero_contato")

        if not all[matricula, rg, cpf, rua, numero_endereco, bairro, cep, numero_contato]:
            messages.error(request, "Todos os campos são obrigatórios")
            return redirect('create_user')
        
        if Usuario.objects.filter(cpf=cpf).exists():
            messages.error(request, "CPF já exisite.")
            return redirect("create-user")
        
        user = Usuario.objects.create_user(
            matricula=matricula,
            rg=rg,
            cpf=cpf,
            rua=rua,
            numero_endereco=numero_endereco,
            bairro=bairro,
            cep=cep,
            numero_contato=numero_contato,
            )

        messages.success(request, f"{matricula} cadastro com sucesso!")
        return redirect('home')

    return render(request, 'user.html')