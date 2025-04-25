from django.shortcuts import render, redirect
from .models import Requerimento
from .forms import RequerimentoForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def lista_requerimentos(request):
    requerimentos = Requerimento.objects.filter(servidor=request.user)
    return render(request, 'lista.html', {'requerimentos': requerimentos})

@login_required
def novo_requerimento(request):
    if request.method == 'POST':
        form = RequerimentoForm(request.POST, request.FILES)
        if form.is_valid():
            req = form.save(commit=False)
            req.servidor = request.user
            req.save()
            return redirect('lista_requerimentos')
    else:
        form = RequerimentoForm()
    return render(request, 'novo.html', {'form': form})