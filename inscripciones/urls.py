from django.urls import path, include
from django.conf.urls import url
from . import views
from .views import *
from django.conf.urls import url

app_name = 'inscripciones'

urlpatterns = [
    path('inscripcion/', views.inscripcion_form, name="inscripcion"),
]