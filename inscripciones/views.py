from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from inscripciones.models import Inscripciones
from inscripciones.forms import*
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy, reverse

# Create your views here.

class RegistroUsuarioInscripcion(CreateView):
    model = User
    second_model = InscripcionesForm
    template_name = "main/inscribirse/inscripcion.html"
    form_class = RegistroForm
    second_form_class = InscripcionesForm
    success_url = reverse_lazy("main:homepage")

    def get_context_data(self, **kwargs):
            context = super(RegistroUsuarioInscripcion, self).get_context_data(**kwargs)
            if 'form' not in context:
                context['form'] = self.form_class(self.request.GET)
            if 'form2' not in context:
                context['form2'] = self.second_form_class(self.request.GET)
            return context
    def post(self, request, *args, **kwargs):
                self.object = self.get_object()
                form = self.form_class(request.POST)
                form2 = self.second_form_class(request.POST)
                if form.is_valid() and form2.is_valid():
                        crear = form.save(commit=False)
                        crear.registro = form2.save()
                        crear.save()
                        return HttpResponseRedirect(self.get_success_url())
                else:
                        return self.render_to_response(self.get_context_data(form=form, form2=form2))

# class RegistroModelo1(CreateView):
#     model = User
#     form_class = RegistroForm
#     template_name = 'main/inscribirse/inscripcion.html'
#     success_url = None

#     def form_valid(self, form):
#         instance_model1 = form.save(commit=False)
#         instance_model1.save()
        
#         return HttpResponseRedirect(reverse('main/inscribirse/inscripcion.html', kwargs={'pk':instance_model1.pk}))

# class InscripcionModel2(CreateView):
#     model =     Inscripciones
#     form_class = InscripcionesForm
#     template_name = 'main/inscribirse/inscripcion.html'
#     success_url = reverse_lazy('main:homepage')

#     def form_valid(self, form):
#         instance_model2 = form.save(commit = False)
#         instance_model2.relacionalModel1 = self.instance_model1
#         instance_model2.save()
        
#         return super(InscripcionModel2, self).form_valid(form)
    
#     def get(self, request, *args, **kwargs):
#         self.instance_model1 = get_object_or_404('User', pk=kwargs.get('pk'))
#         return super(InscripcionModel2, self).get(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         self.instance_model1 = get_object_or_404('User', pk=kwargs.get('pk'))
#         return super(InscripcionModel2, self).get(request, *args, **kwargs)