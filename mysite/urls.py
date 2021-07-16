
from django.contrib import admin
from django.urls import path, include
from main.views import *
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('main.urls', 'main'), namespace='main')),
    path('tinymce/', include('tinymce.urls')),
    path('eliminar_curso/<int:id>/', EliminarCurso, name='eliminar_curso'),
    path('curso_crear/', CursoCrear.as_view(), name="curso_crear"),
    url(r'^editar_curso/(?P<pk>\d+)/$',EditarCurso.as_view(), name="editar_curso"),
    
]
