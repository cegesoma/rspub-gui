#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from rsapp.gui import utils


class Test_utiles(unittest.TestCase):

    def test_languages(self):
        # [print(x) for x in utils.languages()]
        self.assertTrue("en-US" in utils.locales())

    def test_language_index(self):
        print(utils.language_index())