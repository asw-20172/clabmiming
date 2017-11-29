# -*- coding: utf-8 -*-
# @Author: yuselenin
# @Date:   2017-09-13 19:17:00
# @Last Modified by:   yuselenin
# @Last Modified time: 2017-11-29 07:02:23
from django.db import models
from .carrera import Carrera


class Palabra_clave(models.Model):
    nombre = models.CharField(max_length=200)
    carrera = models.ForeignKey(Carrera)

    class Meta:
        verbose_name = "Palabra clave"
        verbose_name_plural = "Palabras claves"

    def __str__(self):
        return self.nombre
