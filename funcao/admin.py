from django.contrib import admin
from .models import Funcao

# Register your models here.

class FuncaoModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Funcao, FuncaoModelAdmin)