from django.contrib import admin
from .models import Curso
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.

class CursoAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Titulo/fecha", {"fields": ["titulo", "publicado"]}),
        ("Contenido", {"fields": ["contenido"]}),
        ("Costo", {"fields": ["costo"]})

    ]
    formfield_overrides= {
        models.TextField:{'widget': TinyMCE()}
    }
admin.site.register(Curso, CursoAdmin)
