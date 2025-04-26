from django.contrib import admin
from .models import TipoRequerimento, Processo

# Register your models here.

admin.site.register(TipoRequerimento)
admin.site.register(Processo)