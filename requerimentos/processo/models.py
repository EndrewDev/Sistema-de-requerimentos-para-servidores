from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Requerimento(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovado', 'Aprovado'),
        ('rejeitado', 'Rejeitado'),
        ('em_analise', 'Em Análise'),
    ]

    servidor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    arquivo_anexo = models.FileField(upload_to='anexos/', blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} ({self.servidor.username})"