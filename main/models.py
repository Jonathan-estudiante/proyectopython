from django.db import models
from datetime import datetime

# Create your models here.

class Curso(models.Model):
    titulo= models.CharField(max_length=200 )
    contenido= models.TextField(max_length=200 )
    publicado= models.DateTimeField(default=datetime.now())
    costo= models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.titulo