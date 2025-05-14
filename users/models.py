from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Usuario(AbstractUser):
    matricula = models.IntegerField(default='000000', verbose_name="Matrícula")
    tipo_usuario = models.CharField(max_length=50, unique=True, verbose_name="Nome usuário", default="Joao Souza")
    rg = models.CharField(max_length=10, default="000-000-000", verbose_name="RG")
    cpf = models.CharField(max_length=11, verbose_name='CPF', default="000-000-000-00")
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name="Endereço")
    number_address = models.FloatField(max_length=5, blank=True, null=True, verbose_name="Número enderenço")
    bairro = models.CharField(max_length=100, default="Centro", blank=False, null=False, verbose_name="Bairro")
    numero_contato = models.CharField(default="(00) 00000-0000", blank=True, null=True, verbose_name="Número contato")

    def __str__(self):
        return self.username
