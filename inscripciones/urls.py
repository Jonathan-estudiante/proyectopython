from django.urls import path
from django.conf.urls import url
from . import views
from .views import *

app_name = 'inscripciones'

urlpatterns = [
    
    path('lista_inscritos/', views.ListaInscritos, name="lista_inscritos"),
    path('eliminar_inscritos/<int:id>/', EliminarInscritos, name='eliminar_inscritos'),
    url(r'^editar_inscritos/(?P<pk>\d+)/$',EditarInscritos.as_view(), name='editar_inscritos'),   
    path('inscripcion/', views.CrearInscripcion, name='inscripcion'),
]