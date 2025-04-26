from django.db import models
from django.conf import settings
from requerimentos.models import Processo

# Create your models here.

class HistoricoMovimentacao(models.Model):
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE, related_name='historico', verbose_name="Processo")
    status = models.CharField(max_length=20, verbose_name="Status")
    responsavel = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name="Responsável pela ação")
    data = models.DateTimeField(auto_now_add=True, verbose_name="Data da movimentação")

    def __str__(self):
        return f"{self.status} - {self.data.strftime('%d/%m/%Y %H:%M')}"