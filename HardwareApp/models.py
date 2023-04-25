from django.db.models import CharField

from django.db import models

#Entidades criadas que não serão modificadas rotineiramente, iremos considera-las como Entidades Estáticas.
class Portas(models.Model):
    Id = models.BigAutoField('Código', auto_created=True, primary_key=True, serialize=False)
    Nome = models.CharField('Nome da Porta', max_length=50, null=False, blank=False)
    Descricao = models.CharField('Descrição da Porta', max_length=256, null=True, blank=True)

    class Meta:
        db_table = 'Portas'

    def __unicode__(self):
        return (self.Nome)
