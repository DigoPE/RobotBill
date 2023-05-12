from django.db.models import CharField

from django.db import models

#Entidades criadas que não serão modificadas rotineiramente, iremos considera-las como Entidades Estáticas.
class Portas(models.Model):
    Id = models.BigAutoField('Código', auto_created=True, primary_key=True, serialize=False)
    Nome = models.CharField('Nome da Porta', max_length=50, null=False, blank=False)
    Descricao = models.CharField('Descrição da Porta', max_length=256, null=True, blank=True)

    class Meta:
        db_table = 'Portas'

    def __str__(self):
        return (self.Nome)


class Placas(models.Model):
    Id = models.BigAutoField('Código', auto_created=True, primary_key=True, serialize=False)
    Porta = models.ForeignKey(Portas, related_name='placas_portas', on_delete=models.PROTECT)
    Nome = models.CharField('Nome da Placa', max_length=50, null=False, blank=False)
    Descricao = models.CharField('Descrição da Placa', max_length=256, null=True, blank=True)

    class Meta:
        db_table = 'Placas'

    def __str__(self):
        return (self.Nome)