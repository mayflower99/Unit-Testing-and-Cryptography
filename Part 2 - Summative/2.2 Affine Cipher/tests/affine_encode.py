from unittest import TestCase

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_encode as ae
from main import affine_decode as ad

from main import convert_to_num as cn
from main import convert_to_text as ct

from main import affine_n_encode as e
from main import affine_n_decode as d

test = "HELLOWORLD"
a = 3
b = 9

class TestAffineEnDecode(TestCase):
    def test_basic(self):
        self.assertEqual("HELLOWORLD", ad(ae(test, 3, 9), 3, 9))

class TextToNumbers(TestCase):
    def test_basic(self):
        self.assertEqual("HELLOWORLD", ct(cn(test), len(test)))

class affine_n_encode(TestCase):
    def test_basic(self):
        test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
        n = 5
        a = 347
        b = 1721
        self.assertEqual(test+"XXXX", d(e(test, n, a, b), n, a, b))

class affine_n_encode_different_A(TestCase):
    def test_basic(self):
        test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
        n = 5
        a = 347
        b = 9490
        self.assertEqual(test+"XXXX", d(e(test, n, a, b), n, a, b))

class affine_n_encode_different_B(TestCase):
    def test_basic(self):
        test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
        n = 5
        a = 9083
        b = 1721
        self.assertEqual(test+"XXXX", d(e(test, n, a, b), n, a, b))
class affine_n_encode_Different_N(TestCase):
    def test_basic(self):
        test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
        n = 7
        a = 347
        b = 1721
        self.assertEqual(test+"XXXXXX", d(e(test, n, a, b), n, a, b))



