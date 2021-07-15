from django import forms
from .models import *

class cursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = {
            'titulo_curso',
            'contenido_curso',
            'fecha_contenido'
        }