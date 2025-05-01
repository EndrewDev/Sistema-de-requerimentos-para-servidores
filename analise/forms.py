from django import forms
from .models import HistoricoMovimentacao


class HistoricoForm(forms.ModelForm):
    class Meta:
        model = HistoricoMovimentacao
        fields = "__all__"