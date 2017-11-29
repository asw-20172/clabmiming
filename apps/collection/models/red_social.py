# -*- coding: utf-8 -*-
# @Author: yuselenin
# @Date:   2017-09-13 19:17:00
# @Last Modified by:   yuselenin
# @Last Modified time: 2017-09-13 21:39:03
from django.db import models


class Red_social(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()

    class Meta:
        verbose_name = "Red social"
        verbose_name_plural = "Redes sociales"

    def __str__(self):
        return self.nombre
