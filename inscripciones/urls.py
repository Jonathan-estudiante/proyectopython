from django.urls import path, include
from django.conf.urls import url
from . import views
from .views import *
from django.conf.urls import url

app_name = 'inscripciones'

urlpatterns = [
    
    path('lista_inscritos/', views.ListaInscritos, name="lista_inscritos"),
    path('inscripcion/', views.inscripcion_form, name="inscripcion"),
    path('eliminar_inscrito/<int:id>/', EliminarInscritos, name='eliminar_inscrito'),
    url(r'^editar_inscritos/(?P<pk>\d+)/$',EditarIncritos.as_view(), name="editar_inscritos"),   
]