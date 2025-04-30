from django.urls import path
from . import views

urlpatterns = [
    path('hostorico/', views.lista_historico, name='lista-historico'),
]
