from django.shortcuts import render
from .models import HistoricoMovimentacao
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required
def lista_historico(request):
    historico = HistoricoMovimentacao.objects.all()
    search = request.GET.get('search')

    if search:
        historico = historico.filter(processo_icontains=search)
    
    return render(request, "listas_historico.html", {'historico': historico})