from django.db import models
from users.models import Usuario

# Create your models here.

class TipoProtocolo(models.Model):
    id = models.IntegerField(primary_key=True ,verbose_name="ID", unique=True)
    titulo = models.CharField(verbose_name="Título")
    descricao = models.CharField(verbose_name="Descrição")

    def __str__(self):
        return f"{self.titulo} (ID: {self.id})"

class Protocolo(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="ID", unique=True)
    tipoprotocolo = models.ForeignKey(TipoProtocolo, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descricao = models.CharField(verbose_name="Descrição")
    
    def __str__(self):
        return f"{self.tipoprotocolo} (ID: {self.id})"
