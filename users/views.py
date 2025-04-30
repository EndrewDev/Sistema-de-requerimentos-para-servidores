from django.shortcuts import render, redirect
from .models import Usuario
# from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.

def create_user(request):
    if request.method == "POST":
        username    = request.POST.get('username')
        password    = request.POST.get("password")
        first_name   = request.POST.get('fisrt_name')
        last_name   = request.POST.get('last_name')
        email       = request.POST.get("email")
        cpf         = request.POST.get("cpf")
        phone       = request.POST.get("phone")
        cep         = request.POST.get("cep")
        address     = request.POST.get("address")   
        number_home = request.POST.get("number_home")

        if not all[username, password, first_name, last_name, email, cpf, phone, cep, address, number_home]:
            messages.error(request, "Todos os campos são obrigatórios")
            return redirect('create_user')
        
        if Usuario.objects.filter(cpf=cpf).exists():
            messages.error(request, "CPF já exisite.")
            return redirect("create-user")
        
        user = Usuario.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            cpf=cpf,
            phone=phone,
            cep=cep,
            address=address,
            number_home=number_home,
            )

        messages.success(request, f"{username} cadastro com sucesso!")
        return redirect('home')

    return render(request, 'user.html')
