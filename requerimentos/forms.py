from django import forms
from .models import TipoRequerimento, Processo

class TiporequerimentosForm(forms.ModelForm):
    class Meta:
        model = TipoRequerimento
        fields = '__all__'

class ProcessoForm(forms.ModelForm):
    class Meta:
        model = Processo
        fields = '__all__'

