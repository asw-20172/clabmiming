# -*- coding: utf-8 -*-
# @Author: yuselenin
# @Date:   2017-09-13 19:17:00
# @Last Modified by:   yuselenin
# @Last Modified time: 2017-09-13 22:34:12
from django.db import models
from .red_social import Red_social


class Consulta(models.Model):
    descripcion = models.CharField(max_length=200)
    red_social = models.ForeignKey(Red_social)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"

    def __str__(self):
        return self.descripcion
