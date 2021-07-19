from django import forms
from .models import *
from inscripciones.forms import *
from django.contrib.auth.models import User

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = [
            'titulo',
            'contenido',
            'publicado',
            'costo',
        ]
