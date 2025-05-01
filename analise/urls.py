from django.urls import path
from . import views

urlpatterns = [
    path('listas_historicos/', views.lista_historico, name='listas-historicos'),
    path('listas_historicos/detalhe/<int:pk>/', views.historico_detalhe, name="datelhe-historico"),
    path('criar_historico/', views.criar_historico, name="criar-historico"),
]
