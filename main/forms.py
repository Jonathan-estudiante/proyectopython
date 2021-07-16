from django import forms
from .models import *

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = (
            'titulo',
            'contenido',
            'publicado',
            'costo'
        )