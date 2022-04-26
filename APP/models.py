from django.db import models

# Create your models here.

class Tanulo(models.Model):
    
    nev = models.CharField(max_length=32)
    om = models.CharField(max_length=11)
    pontszam = models.FloatField()
    A_eredmeny = models.BooleanField()
    B_eredmeny = models.BooleanField()
    C_eredmeny = models.BooleanField()
    D_eredmeny = models.BooleanField()
    E_eredmeny = models.BooleanField()
    F_eredmeny = models.BooleanField()
    
    
    
    
    
    class Meta:
        verbose_name = 'Tanulo'
        verbose_name_plural = 'Tanulok'

    def __str__(self):
        pass
