from django.db import models

# Create your models here.

class Feira(models.Model):
    long = models.FloatField()
    lat = models.FloatField()
    setcens = models.DecimalField(max_digits=15, decimal_places=0)
    areap = models.DecimalField(max_digits=13, decimal_places=0)
    coddist = models.DecimalField(max_digits=3, decimal_places=0)
    distrito = models.TextField()
    codsubpref = models.DecimalField(max_digits=2, decimal_places=0)
    subpref = models.TextField()
    regiao5 = models.TextField()
    regiao8 = models.TextField()
    nome_feira = models.TextField()
    registro = models.TextField(max_length=6)
    logradouro = models.TextField()
    numero = models.TextField(blank=True, null=True)
    bairro = models.TextField()
    referencia = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome_feira