from django.urls import path
from . import views

urlpatterns = [
    path('listas_funcao/', views.listas_funcao, name='listas-funcao'),
    path('criado_funcao/', views.criado_funcao, name='criado-funcao'),
    path('atualizado-funcao/<int:pk>/', views.atualizacao_funcao, name="atulizado-funcao"),
    path('deleta-funcao/<int:pk>/', views.deleta_funcao, name='deleta-funcao'),
]
