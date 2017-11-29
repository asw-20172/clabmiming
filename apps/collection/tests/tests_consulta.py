# -*- coding: utf-8 -*-
# @Author: yuselenin
# @Date:   2017-11-29 05:45:11
# @Last Modified by:   yuselenin
# @Last Modified time: 2017-11-29 07:25:55
from django.test import TestCase

from ..models.consulta import Consulta
from ..models.red_social import Red_social


class ConsultaTestCase(TestCase):

    def setUp(self):
        Red_social.objects.create(
            nombre="Red_social 3", descripcion="Descripcion")
        red_social3 = Red_social.objects.get(nombre="Red_social 3")
        Consulta.objects.create(
            descripcion="Consulta 1", red_social=red_social3)
        Consulta.objects.create(
            descripcion="Consulta 2", red_social=red_social3)

    def test_srt(self):
        obj = Consulta.objects.get(descripcion="Consulta 1")
        self.assertAlmostEqual(obj.__str__(), "Consulta 1")
