from django.shortcuts import render, redirect
from .models import Usuario
# from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.

def create_user(request):
    if request.method == "POST":
        matricula      = request.POST.get('matricula')
        tipo_ususario  = request.POST.get('username')
        rg             = request.POST.get('rg')
        cpf            = request.POST.get("cpf")
        address        = request.POST.get("address")   
        number_address = request.POST.get("number_address")
        bairro         = request.POST.get('bairro')
        numero_contato = request.POST.get("numero_contato")

        if not all[matricula, tipo_ususario, rg, cpf, address, number_address, bairro, numero_contato]:
            messages.error(request, "Todos os campos são obrigatórios")
            return redirect('create_user')
        
        if Usuario.objects.filter(cpf=cpf).exists():
            messages.error(request, "CPF já exisite.")
            return redirect("create-user")
        
        user = Usuario.objects.create_user(
            matricula=matricula,
            tipo_ususario=tipo_ususario,
            rg=rg,
            cpf=cpf,
            address=address,
            number_address=number_address,
            bairro=bairro,
            numero_contato=numero_contato,
            )

        messages.success(request, f"{tipo_ususario} cadastro com sucesso!")
        return redirect('home')

    return render(request, 'user.html')
