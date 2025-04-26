from django.contrib import admin
from .models import Usuario

# Register your models here.

class UsuarioModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Usuario, UsuarioModelAdmin)
