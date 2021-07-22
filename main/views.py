from django.shortcuts import render, redirect
from django.db.models import Sum 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy
from .models import Curso
from .forms import*
from inscripciones.models import*
# Función para redireccionarse a la página principal
def homepage(request):
    return render(request, "main/inicio.html", {"cursos": Curso.objects.all()})
# Función para crear un usuario
def RegistroUsuario(request):

    if request.method == "POST":
        form_registro = UserCreationForm(request.POST)
        if form_registro.is_valid():
            usuario = form_registro.save()
            nombre_usuario = form_registro.cleaned_data.get('username')
            messages.success(
                request, f"Nueva Cuenta Creada : {nombre_usuario}")
            login(request, usuario)
            messages.info(request, f"Has sido logeado como {nombre_usuario}")
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form_registro = UserCreationForm
    return render(request, "main/registro.html", {"form_registro": form_registro})
# Función para salir de la página
def logout_request(request):
    logout(request)
    messages.info(request, "Saliste exitosamente") 
    return redirect("main:homepage")
# Función para entrar si ya estamos registrado
def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contraseña)

            if user is not None:
                login(request, user)
                messages.info(request, f"Estás logeado como {usuario}")
                return redirect("main:homepage")
            else:
                messages.error(request, "Usuario o contraseña equivocada")
        else:
            messages.error(request, "Usuario o contraseña equivocada")
    form = AuthenticationForm()
    return render(request, "main/login.html", {"form": form})
# Clase para crear un curso
class CursoCrear(CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'main/curso_crear.html'
    success_url = reverse_lazy('main:lista_cursos')
# Función para crear una lista de los cursos que hayan
def CursoLista(request):
    cursos = Curso.objects.all()
    contexto = {
        'cursos': cursos
    }
    return render(request, 'main/lista_cursos.html', contexto)
# Clase para editar un curso
class EditarCurso(UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'main/editar_curso.html'
    success_url = reverse_lazy('main:lista_cursos')
# Función para eliminar un curso
def EliminarCurso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    return redirect("main:lista_cursos")
# Función para ver una lista de personas inscritas en un curso específico
def listaCurso(request, id):
    curso = Curso.objects.get(id=id)
    inscritos_curso = Inscripciones.objects.filter(nombre_curso = curso)
    suma_costos = inscritos_curso.aggregate(Sum('costo_total'))
    
    contexto = {
        'curso': curso,
        'inscritos': inscritos_curso,
        'suma':suma_costos,
    }
    return render(request, 'inscripciones/lista_inscritos.html', contexto)