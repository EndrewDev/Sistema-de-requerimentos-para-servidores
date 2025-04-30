from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Usuario(AbstractUser):
    username = models.CharField(max_length=50, unique=True, verbose_name="Nome usuário", default="Joao Souza")
    first_name = models.CharField(max_length=20, verbose_name="Primeiro nome", default='João')
    last_name = models.CharField(max_length=20, verbose_name="Segudno nome", default="Souza")
    email = models.CharField(verbose_name="E-mail", default="joao.souza@gmail.com")
    cpf = models.CharField(max_length=11, verbose_name='CPF', default="000-000-000-00")
    phone = models.CharField(max_length=10, verbose_name="Telefone", default="(00) 0000-0000")
    cep = models.CharField(max_length=9, default='00000-000')
    address = models.CharField(max_length=255, verbose_name="Endereço", default="Sem endereço")
    number_home = models.FloatField(max_length=5, verbose_name="Número na casa", default="000")

    def __str__(self):
        return self.username
