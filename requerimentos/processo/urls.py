from django.urls import path
from. import views

urlpatterns = [
    path('', views.lista_requerimentos, name='listas_requerimentos'),
    path('novo/', views.novo_requerimento, name='novo_requerimento'),
]
