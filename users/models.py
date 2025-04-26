from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Usuario(AbstractUser):
    is_colaborador = models.BooleanField(default=False)
    full_name = models.CharField(max_length=100, verbose_name="Nome completo")
    username = models.CharField(max_length=50, verbose_name="Usuário")
    email = models.CharField(max_length=200, verbose_name="E-mail")
    cpf = models.FloatField(max_length=11, verbose_name="CPF")
    phone = models.FloatField(verbose_name="Telefone")
    cep = models.FloatField(verbose_name="CEP")
    address = models.CharField(max_length=200, verbose_name="Enderço")
    number_home = models.FloatField(verbose_name="Número de casa")
    position = models.    

    def __str__(self):
        return self.username
