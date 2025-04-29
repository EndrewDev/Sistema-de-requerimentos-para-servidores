from django.urls import path
import views

urlpatterns = [
    path('hostorico/', views.lista_historico, name='lista-historico'),
]
