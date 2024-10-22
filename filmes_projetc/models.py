from django.db import models

# Create your models here.
class Filmes(models.Model):
    id = models.IntegerField(primary_key=True, blank=False)
    nome = models.CharField(max_length=100, blank=False)
    genero = models.CharField(max_length=100, blank=True)
    ano = models.IntegerField(blank=False)

    def __str__(self):
        return self.nome