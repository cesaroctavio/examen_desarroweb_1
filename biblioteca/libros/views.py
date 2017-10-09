# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import libro

# Create your views here.

def home(request):
    print request
    titulo = "libro"
    return render(request, "home.html", {"Titulo" : titulo})

def lista_libros(request):
    result_set = libro.objects.all()
    context = {
    "result": result_set
    }
    return render(request, "lista_libros.html", context)

def detalle_libro(request, id=10):
    result_set = libro.objects.get(id=id)
    context = {
    "result": result_set
    }
    return render(request, "datalle_libro.html", context)
