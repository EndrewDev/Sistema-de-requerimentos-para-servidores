from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from .models import TipoRequerimento, Processo

@receiver(pre_save, sender=TipoRequerimento)
def TiporequerimentoPresave(sender, instance, **kwargs):
    print(" Já está no banco de dados ")

@receiver(post_save, sender=TipoRequerimento)
def Tiporequerimento_Post_save(sender, instance, **kwargs):
    print(" Já está no banco de dados ")

@receiver(pre_delete, sender=TipoRequerimento)
def Tiporequerimento_pre_delete(sender, instance, **kwargs):
    print(" Já está deletado no banco de dados")

@receiver(post_delete, sender=TipoRequerimento)
def Tiporequerimento_post_delete(sender, instance, **kwargs):
    print(" Já está deletado no banco de dados")

@receiver(pre_save, sender=Processo)
def Processo_Pre_save(sender, instance, **kwargs):
    print(" Já está no banco de dados ")

@receiver(post_save, sender=Processo)
def Processo_post_save(sender, instance, **kwargs):
    print(" Já está no banco de dados ")

@receiver(pre_delete, sender=Processo)
def Processo_pre_delete(sender, instance, **kwargs):
    print(" Já está deletado no banco de dados ")

@receiver(post_delete, sender=Processo)
def Processo_post_delete(sender, instance, **kwargs):
    print(" Já está deletado no banco de dados ")