from django.contrib import admin
from .models import Inscripciones
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.

class InscripcionesAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Usuario", {"fields": ["usuario"]}),
        ("Fecha", {"fields": ["fecha_registro_curso"]}),
        ("Curso", {"fields": ["nombre_curso"]}),
        ("Costo", {"fields": ["costo_total"]})

    ]
    formfield_overrides= {
        models.TextField:{'widget': TinyMCE()}
    }

admin.site.register(Inscripciones, InscripcionesAdmin)