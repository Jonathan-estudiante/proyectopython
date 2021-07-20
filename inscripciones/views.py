from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from inscripciones.models import Inscripciones
from inscripciones.forms import*
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy, reverse

# Create your views here.

def RegistroUsuarioInscripcion(request):

    if request.method == "POST":      
        form_registro = RegistroForm(request.POST, prefix="registro_form")
        form_inscripcion = InscripcionesForm(reques.POST, prefix="inscripcion_form")
        if form_registro.is_valid() and form_inscripcion.is_valid():  
            estudiante = form_registro.save(commit=False)
            estudiante.user = request.user
            estudiante.save()

            inscripcion = form_inscripcion.save(commit=False)
            inscripcion.usuario = estudiante 
            inscripcion.save()
    else:   
        form_registro = RegistroForm(prefix="registro_form")
        form_inscripcion = InscripcionesForm(prefix="inscripcion_form")
        context = { 'form' : form_registro, 'form2' : form_inscripcion }

    return render(request, 'main/inscribirse/inscripcion.html',  context)