# -*- coding: utf-8 -*-
# @Author: yuselenin
# @Date:   2017-09-13 19:17:00
# @Last Modified by:   yuselenin
# @Last Modified time: 2017-09-13 22:27:31
from django.db import models


class Carrera(models.Model):
    nombre = models.CharField(max_length=64)
    nombre_corto = models.CharField(max_length=16)
    titulo = models.CharField(max_length=64)

    class Meta:
        verbose_name = "Carrera"
        verbose_name_plural = "Carreras"

    def __str__(self):
        return self.nombre
