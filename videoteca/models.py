from django.db import models

class Gioco(models.Model):
    titolo = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100)
    anno = models.IntegerField()
    genere = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return f'{self.titolo} di {self.categoria}'