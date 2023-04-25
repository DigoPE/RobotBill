from django.db.models import CharField

from django.db import models


class Temas(models.Model):
    Assunto = models.CharField('Assunto', max_length=20, primary_key=True)
    Descricao = models.CharField('Descrição', max_length=250, null=True, blank=True)
    class Meta:
        db_table = 'Temas'

    def __unicode__(self):
        return (self.Assunto)

#Entidades criadas que não serão modificadas rotineiramente, iremos considera-las como Entidades Estáticas.
class Interacao(models.Model):
    Id = models.BigAutoField('Código', auto_created=True, primary_key=True, serialize=False)
    Contato = models.TextField('Descrição ou Pergunta para Interação', null=False, blank=False)
    TratoResp = models.TextField('Resposta da Interação', null=False, blank=False)
    Tema = models.ForeignKey(Temas, related_name='interacao_tema', on_delete=models.PROTECT)

    class Meta:
        db_table = 'Interacao'

    def __unicode__(self):
        return (self.Contato)
