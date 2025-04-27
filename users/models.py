from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Usuario(AbstractUser):
    is_colaborador = models.BooleanField(default=False)
    email = models.CharField(max_length=200, verbose_name="E-mail")
    # position = models.CharField()    

    def __str__(self):
        return self.is_colaborador
