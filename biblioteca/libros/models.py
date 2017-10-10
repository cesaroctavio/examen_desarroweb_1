# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils import timezone

from django.conf import settings

class libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    editorial = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=32)
    precio = models.IntegerField()
    creado = models.DateTimeField(default = timezone.now)

def __str__(self):
    return str(self.titulo)
