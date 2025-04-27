from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.

def create_user(request):
    if request.method == "POST":
        full_name   = request.POST.get("full_name")
        username    = request.POST.get('username')
        password    = request.POST.get("password")
        email       = request.POST.get("email")
        cpf         = request.POST.get("cpf")
        phone       = request.POST.get("phone")
        cep         = request.POST.get("cep")
        address     = request.POST.get("address")   
        number_home = request.POST.get("number_home")
        # position    = request.POST.get("position")

        if not all[full_name, username, password, email, cpf, phone, cep, address, number_home]:
            messages.error(request, "Todos os campos são obrigatórios")
            return redirect('create_user')
        
        if Usuario.objects.filter(cpf=cpf).exists():
            messages.error(request, "CPF já exisite.")
            return redirect("create_user")
        
        user = Usuario.objects.create_user(
            full_name=full_name,
            username=username,
            password=password,
            email=email,
            cpf=cpf,
            phone=phone,
            cep=cep,
            address=address,
            number_home=number_home,
            # position=position,
        )

        messages.success(request, f"{full_name} cadastro com sucesso!")
        return redirect('home')

    return render(request, 'user.html')
