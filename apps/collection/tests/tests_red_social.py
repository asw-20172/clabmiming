# -*- coding: utf-8 -*-
# @Author: yuselenin
# @Date:   2017-11-29 05:45:11
# @Last Modified by:   yuselenin
# @Last Modified time: 2017-11-29 06:57:25
from django.test import TestCase

from ..models.red_social import Red_social


class Red_socialTestCase(TestCase):

    def setUp(self):
        Red_social.objects.create(
            nombre="Red_social 1", descripcion="Descripcion")
        Red_social.objects.create(
            nombre="Red_social 2", descripcion="Descripcion")

    def test_srt(self):
        obj = Red_social.objects.get(nombre="Red_social 1")
        self.assertAlmostEqual(obj.__str__(), "Red_social 1")
