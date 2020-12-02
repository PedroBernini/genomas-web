from django.db import models

class DataSetPermutation(models.Model):
    nome = models.CharField('nome', blank=False, null=False, default="Dataset", max_length=255)
    permutacoes = models.TextField('permutacoes', blank=False, null=False)
    tamanho_permutacao = models.IntegerField('tamanho_permutacao', blank=False, null=False)
    quantidade = models.IntegerField('quantidade', blank=False, null=False)
    minimo_breakpoints = models.IntegerField('minimo_breakpoints', blank=True, null=True)
    maximo_breakpoints = models.IntegerField('maximo_breakpoints', blank=True, null=True)
