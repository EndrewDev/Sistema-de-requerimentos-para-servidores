from django.db import models

# Create your models here.

class Funcao(models.Model):
    id = models.IntegerField(primary_key=True ,verbose_name="ID", unique=True)
    titulo = models.CharField(verbose_name="Título", unique=True)
    descricao = models.CharField(verbose_name="Descrição")

    def __str__(self):
        return f"{self.titulo} (ID: {self.id})"