# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import libro

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .forms import LibroModelForm
from .mixin import FormUserNeededMixin
from django.urls import reverse_lazy
from django.db.models import Q


from django.conf import settings
# Create your views here.
def home_libros(request):
    print request
    titulo = "libro"
    return render(request, "libros/home_libros.html", {"Titulo" : titulo})



def detalle_libro(request, id=10):
    result_set = libro.objects.get(id=id)
    context = {
    "result": result_set
    }
    return render(request, "libros/detalle_libro.html", context)

class LibroCreateView(FormUserNeededMixin, CreateView):
    form_class = LibroModelForm
    template_name = "libros/CrearLibro_view.html"
    success_url = "/libros/lista"
    login_url = "/admin"

class LibroUpdateView(UpdateView):
    queryset = libro.objects.all()
    form_class = LibroModelForm
    template_name = "libros/Actualizar_view.html"
    success_url = "/libros/lista"

class LibroDeleteView(LoginRequiredMixin, DeleteView):
    model = libro
    template_name = "libros/Delete_confirm.html"
    success_url = reverse_lazy("list")

class LibroListView(ListView):
    template_name = "libros/lista_libros.html"

    def get_queryset(self, *args, **kwargs):
        qs = libro.objects.all()
        print self.request.GET
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
            Q(Nombre__icontains=query)|
            Q(user__username__icontains=query)
            )
        return qs
    def get_context_data(self, *args, **kwargs):
         context = super(LibroListView, self).get_context_data(*args, **kwargs)
         print context
         context['create_form'] = LibroModelForm()
         context['create_url'] = reverse_lazy("Libro_create")
         return context
