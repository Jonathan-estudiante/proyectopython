from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',

        ]
        labels = {
            'username': 'Nombre de usuario',
        }


class InscripcionesForm(forms.ModelForm):
    class Meta:
        model = Inscripciones
        fields = (
            'fecha_registro_curso',
            'nombre_curso',
            'costo_total',
        )
        labels = {
            'fecha_registro_curso': 'Fecha de Inscripción',
            'nombre_curso': 'Nombre del curso',
        }
        widgets = {
            'nombre_curso': forms.Select(attrs={'class': 'form-control'}),
        }

