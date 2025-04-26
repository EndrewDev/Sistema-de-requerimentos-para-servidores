from django.db import models
from django.conf import settings

# Create your models here.

class TipoRequerimento(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    texto_padrao = models.TextField(verbose_name="Texto padrão")
    documentos_obrigatorios = models.TextField(help_text="Separe por vírgula", verbose_name="Documentos obrigatórios")

    def __str__(self):
        return self.titulo
    
class Processo(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aceito', 'Aceito'),
        ('devolvido', 'Devolvido'),
        ('em_tramitacao', 'Em tramitação'),
    ]

    servidor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Servidor")
    tipo = models.ForeignKey(TipoRequerimento, on_delete=models.CASCADE, verbose_name="Tipo de requerimento")
    documentos = models.FileField(upload_to='documentos/', verbose_name="Documentos Anexados")
    info_complementar = models.TextField(blank=True, null=True, verbose_name="Informações complementaes")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente', verbose_name="Status")
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name="Atualizado em'")
    bloqueado = models.BooleanField(default=False, verbose_name="Bloqueado para edição")

    def __str__(self):
        return f"{self.tipo.titulo} - {self.servidor.username}"
