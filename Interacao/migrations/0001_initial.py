# Generated by Django 4.1.2 on 2023-04-08 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Temas',
            fields=[
                ('Assunto', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Assunto')),
                ('Descricao', models.CharField(blank=True, max_length=250, null=True, verbose_name='Descrição')),
            ],
            options={
                'db_table': 'Temas',
            },
        ),
        migrations.CreateModel(
            name='Interacao',
            fields=[
                ('Id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Código')),
                ('Contato', models.TextField(verbose_name='Descrição ou Pergunta para Interação')),
                ('TratoResp', models.TextField(verbose_name='Resposta da Interação')),
                ('Tema', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='interacao_tema', to='Interacao.temas')),
            ],
            options={
                'db_table': 'Interacao',
            },
        ),
    ]
