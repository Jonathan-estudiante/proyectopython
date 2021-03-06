from django.shortcuts import render,  redirect
from inscripciones.forms import*
from django.views.generic import UpdateView, ListView, DeleteView
from django.urls import reverse_lazy
from urllib import request

# Create your views here.

def CrearInscripcion(request):
    form_registro = RegistroForm(prefix="registro_form")
    form_inscripcion = InscripcionesForm(prefix="inscripcion_form")
    context = { 
            'form_registro' : form_registro, 
            'form_inscripcion' : form_inscripcion,
            }
    if request.method == "POST":      
        form_registro = RegistroForm(request.POST, prefix="registro_form")
        form_inscripcion = InscripcionesForm(request.POST, prefix="inscripcion_form")
        if form_registro.is_valid() and form_inscripcion.is_valid():  
            estudiante = form_registro.save(commit=False)
            estudiante.user = request.user
            estudiante.save()

            inscripcion = form_inscripcion.save(commit=False)
            inscripcion.usuario = estudiante 
            inscripcion.save()
            return render(request, 'inscripciones/lista_inscritos.html', context)
            

    return render(request, 'inscripciones/inscripcion_form.html',  context)

def ListaInscritos(request):
    inscritos = Inscripciones.objects.all()
    contexto = {
        'inscritos': inscritos
    }
    return render(request, 'inscripciones/lista_inscritos.html', contexto)

def EliminarInscritos(request, id):
    inscritos = Inscripciones.objects.get(id=id)
    inscritos.delete()
    return redirect("inscripciones:lista_inscritos")
    
class EditarInscritos(UpdateView):
    model = Inscripciones
    form_class = InscripcionesForm
    template_name = 'inscripciones/editar_inscritos.html'
    success_url = reverse_lazy("inscripciones:lista_inscritos")

