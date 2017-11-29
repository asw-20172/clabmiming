# -*- coding: utf-8 -*-
# @Author: yuselenin
# @Date:   2017-11-29 05:45:11
# @Last Modified by:   yuselenin
# @Last Modified time: 2017-11-29 07:30:25
from django.test import TestCase

from ..models.data_red_social import Data_red_social


class CarreraTestCase(TestCase):

    def setUp(self):
        Data_red_social.objects.create(
            titulo="Titulo 1",
            descripcion_empleo="Descripcion",
            lugar="Lugar",
            funciones_laborales="funciones_laborales",
            institucion="institucion",
            sector="sector",
            tipo_empleo="tipo_empleo",
        )

    def test_srt(self):
        obj = Data_red_social.objects.get(titulo="Titulo 1")
        self.assertAlmostEqual(obj.__str__(), "Titulo 1")
