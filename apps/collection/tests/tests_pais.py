# -*- coding: utf-8 -*-
# @Author: yuselenin
# @Date:   2017-11-29 05:45:11
# @Last Modified by:   yuselenin
# @Last Modified time: 2017-11-29 06:57:07
from django.test import TestCase

from ..models.pais import Pais


class PaisTestCase(TestCase):

    def setUp(self):
        Pais.objects.create(
            nombre="Pais 1")
        Pais.objects.create(
            nombre="Pais 2")

    def test_srt(self):
        obj = Pais.objects.get(nombre="Pais 1")
        self.assertAlmostEqual(obj.__str__(), "Pais 1")
