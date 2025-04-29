from django.urls import path
import views

urlpatterns = [
    
    # Tipo requerimento:
    path('listas_tiporequerimento/', views.listas_tiporequerimento, name='tiporequerimento'),
    path('listas_tiporequerimento/criado_requerimento', views.create_requerimento, name='create-requerimento'),
    path('listas_tiporequerimento/atualizado/<int:pk>/', views.atualizar_requerimento, name='atualizado-requerimento'),
    path('listas_tiporequerimento/deletar/<int:pk>/', views.delete_requerimento, name='delete-requerimento'),

    # Processo
    path('listas_processo/', views.listas_processo, name='processo'),
    path('listas_processo/criado/', views.criado_processo, name='criado-processo'),
    path('listas_processo/atualido/<int:pk>/', views.atualizar_processo, name='atualizado-processo'),
    path('listas_processo/deleta/<int:pk>/', views.delete_processo, name='deleta-processo'),
]
