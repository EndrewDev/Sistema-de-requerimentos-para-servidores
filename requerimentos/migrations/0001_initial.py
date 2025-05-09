# Generated by Django 5.2 on 2025-04-26 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Processo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documentos', models.FileField(upload_to='documentos/', verbose_name='Documentos Anexados')),
                ('info_complementar', models.TextField(blank=True, null=True, verbose_name='Informações complementaes')),
                ('status', models.CharField(choices=[('pendente', 'Pendente'), ('aceito', 'Aceito'), ('devolvido', 'Devolvido'), ('em_tramitacao', 'Em tramitação')], default='pendente', max_length=20, verbose_name='Status')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name="Atualizado em'")),
                ('bloqueado', models.BooleanField(default=False, verbose_name='Bloqueado para edição')),
            ],
        ),
        migrations.CreateModel(
            name='TipoRequerimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('texto_padrao', models.TextField(verbose_name='Texto padrão')),
                ('documentos_obrigatorios', models.TextField(help_text='Separe por vírgula', verbose_name='Documentos obrigatórios')),
            ],
        ),
    ]
