from django.db import models
from django.contrib.auth.models import AbstractUser
from tipo_usuario.models import TipoUsuario
from funcao.models import Funcao

# Create your models here.
class Usuario(AbstractUser):
    id = models.IntegerField(primary_key=True, verbose_name=("ID"), unique=True)
    matricula = models.IntegerField(default='000000', verbose_name="Matrícula", unique=True)
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11, default="000-000-000-00", verbose_name="CPF")
    rg = models.CharField(max_length=10, default="000-000-000", verbose_name="RG")
    rua = models.CharField(max_length=255, blank=True, null=True, verbose_name="Endereço")
    numero_endereco = models.FloatField(max_length=5, blank=True, null=True, verbose_name="Número endereço")
    bairro = models.CharField(max_length=100, default="Centro", blank=False, null=False, verbose_name="Bairro")
    cep = models.CharField(default="00000-000", verbose_name="CEP")
    numero_contato = models.CharField(default="(00) 00000-0000", blank=True, null=True, verbose_name="Número contato")
    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.matricula
