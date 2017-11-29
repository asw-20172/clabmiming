# -*- coding: utf-8 -*-
# @Author: yuselenin
# @Date:   2017-11-29 05:45:11
# @Last Modified by:   yuselenin
# @Last Modified time: 2017-11-29 06:56:57
from django.test import TestCase

from ..models.carrera import Carrera


class CarreraTestCase(TestCase):

    def setUp(self):
        Carrera.objects.create(
            nombre="Carrera 1", nombre_corto="Descripcion", titulo="Titulo")
        Carrera.objects.create(
            nombre="Carrera 2", nombre_corto="Descripcion", titulo="Titulo")

    def test_srt(self):
        obj = Carrera.objects.get(nombre="Carrera 1")
        self.assertAlmostEqual(obj.__str__(), "Carrera 1")
