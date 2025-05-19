from django.db import models
from users.models import Usuario

# Create your models here.

class Setor(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="ID", unique=True)
    titulo = models.CharField(verbose_name="Título", unique=True)
    usuarios = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} (ID: {self.id})"