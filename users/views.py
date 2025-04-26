from django.shortcuts import render
from .models import Usuario
from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.

def create_user(request):
    if request.method == "POST":
        full_name   = request.POST.get("full_name")
        username    = request.POST.get("username")
        password    = request.POST.get("password")
        email       = request.POST.get("email")
        cpf         = request.POST.get("cpf")
        phone       = request.POST.get("phone")
        cep         = request.POST.get("cep")
        address     = request.POST.get("address")
        number_home = request.POST.get("number_home")
        position    = request.POST.get("position")




