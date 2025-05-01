from django.shortcuts import render, get_object_or_404, redirect
from .models import HistoricoMovimentacao
from .forms import HistoricoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required
def lista_historico(request):
    historico = HistoricoMovimentacao.objects.all()
    search = request.GET.get('search')

    if search:
        historico = historico.filter(processo_icontains=search)
    
    return render(request, "listas_historicos.html", {'historico': historico})

@login_required
def historico_detalhe(request, pk):
    historico = get_object_or_404(HistoricoMovimentacao, pk=pk)
    return render(request, 'detalhe.html', {'detalhe': historico})

@login_required
def criar_historico(request):

    if request == "POST":
        historico_forms = HistoricoForm(request.POST)
        if historico_forms.is_valid():
            historico_forms.save()
            messages.success(request, "Histórico criano com sucesso")
            return redirect('listas-historicos')
    else:
        historico_forms = HistoricoForm()

    return render(request, 'criar-historico.html', {'historico-criar': historico_forms})
