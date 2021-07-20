from django.urls import path, include
from django.conf.urls import url
from . import views
from .views import *
from django.conf.urls import url

app_name = 'main'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('registro/', views.RegistroUsuario, name="registro"),
    path('logout/', views.logout_request, name="logout"),
    path('login/', views.login_request, name="login"),
    path('lista_cursos/', views.CursoLista, name="lista_cursos"),
    path('eliminar_curso/<int:id>/', EliminarCurso, name='eliminar_curso'),
    path('curso_crear/', CursoCrear.as_view(), name="curso_crear"),
    url(r'^editar_curso/(?P<pk>\d+)/$',EditarCurso.as_view(), name="editar_curso"),    

]
