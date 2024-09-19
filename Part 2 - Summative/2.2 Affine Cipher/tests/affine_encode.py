from unittest import TestCase

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_encode as ae
from main import affine_decode as ad

test = "HELLOWORLD"
a = 3
b = 9

class TestInsertString(TestCase):
    def test_basic(self):
        self.assertEqual("HELLOWORLD", ad(ae(test, 3, 0), 3, 0))



