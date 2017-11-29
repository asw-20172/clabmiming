# -*- coding: utf-8 -*-
# @Author: yuselenin
# @Date:   2017-09-13 19:17:00
# @Last Modified by:   yuselenin
# @Last Modified time: 2017-09-13 21:37:47
from django.db import models


class Data_red_social(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion_empleo = models.TextField()
    lugar = models.CharField(max_length=100)
    funciones_laborales = models.CharField(max_length=200)
    # TODO: review can move other table
    institucion = models.CharField(max_length=200)
    nivel_de_experiencia = models.CharField(max_length=200)
    sector = models.CharField(max_length=200)
    tipo_empleo = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Data red social"
        verbose_name_plural = "Data redes sociales"

    def __str__(self):
        return self.titulo
