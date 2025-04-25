from django import forms
from .models import Requerimento

class RequerimentoForm(forms.ModelForm):
    class Meta:
        model = Requerimento
        fields = ['titulo', 'descricao', 'arquivo_anexo']
