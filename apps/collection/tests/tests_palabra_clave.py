# -*- coding: utf-8 -*-
# @Author: yuselenin
# @Date:   2017-11-29 05:45:11
# @Last Modified by:   yuselenin
# @Last Modified time: 2017-11-29 06:59:55
from django.test import TestCase

from ..models.palabra_clave import Palabra_clave
from ..models.carrera import Carrera


class Palabra_claveTestCase(TestCase):

    def setUp(self):
        Carrera.objects.create(
            nombre="Carrera 3", nombre_corto="Descripcion", titulo="Titulo")
        carrera3 = Carrera.objects.get(nombre="Carrera 3")
        Palabra_clave.objects.create(
            nombre="Palabra_clave 1",
            carrera=carrera3
        )
        Palabra_clave.objects.create(
            nombre="Palabra_clave 2",
            carrera=carrera3
        )

    def test_srt(self):
        obj = Palabra_clave.objects.get(nombre="Palabra_clave 1")
        self.assertAlmostEqual(obj.__str__(), "Palabra_clave 1")
