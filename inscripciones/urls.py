from django.urls import path, include
from django.conf.urls import url
from . import views
from .views import *
from django.conf.urls import url

app_name = 'inscripciones'

urlpatterns = [
    path('inscripcion/', RegistroUsuarioInscripcion.as_view(), name="inscripcion"),
    # path('inscripcion/', InscripcionModel2.as_view(), name="inscripcion"),
]