from django.db import models
from datetime import datetime
from django.forms import DecimalField
from main.models import *
from django.contrib.auth.models import User

# Create your models here.
class Usuario(User):
    class Meta:
        proxy = True

class Inscripciones(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_registro_curso = models.DateTimeField(default=datetime.now())
    nombre_curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    costo_total = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return '{}'.format(self.nombre_curso)

