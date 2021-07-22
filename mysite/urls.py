from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('main.urls', 'main'), namespace='main')),
    path('', include(('inscripciones.urls', 'inscripciones'), namespace='inscripciones')),
    path('tinymce/', include('tinymce.urls')),
    url( r'^ select2 /' ,  include ( 'select2.urls' )), 

]
