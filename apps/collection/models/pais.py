# -*- coding: utf-8 -*-
# @Author: yuselenin
# @Date:   2017-09-13 19:17:00
# @Last Modified by:   yuselenin
# @Last Modified time: 2017-09-13 21:38:10
from django.db import models


class Pais(models.Model):
    nombre = models.CharField(max_length=64)

    class Meta:
        verbose_name = "Pais"
        verbose_name_plural = "Paises"

    def __str__(self):
        return self.nombre
