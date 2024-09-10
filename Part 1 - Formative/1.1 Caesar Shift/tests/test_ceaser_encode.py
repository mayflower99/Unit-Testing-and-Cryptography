from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import caesar_encode as ce
from main import caesar_decode as cd


class TestInsertString(TestCase):
    def test_blank_equals_blank(self):
        self.assertEqual(ce("", 10), "")
    def test_n_equals_0(self):
        self.assertEqual("thequickbrownfoxjumpsoverthelazydog", cd(ce("thequickbrownfoxjumpsoverthelazydog", 0), 0))
    def test_n_equals_256(self):
        self.assertEqual("thequickbrownfoxjumpsoverthelazydog", cd(ce("thequickbrownfoxjumpsoverthelazydog", 0), 256))
    def test_n_equals_negitive(self):
        self.assertEqual("thequickbrownfoxjumpsoverthelazydog", cd(ce("thequickbrownfoxjumpsoverthelazydog", 0), -256))
    def test_spaces(self):
        self.assertEqual("the quick brown fox jumps over the lazy dog", cd(ce("the quick brown fox jumps over the lazy dog", 0), 256))
    def test_capitals(self):
        self.assertEqual("TheQuickBrownFoxJumpsOverTheLazyDog", cd(ce("TheQuickBrownFoxJumpsOverTheLazyDog", 50), 50))
    def test_special_charaters(self):
        self.assertEqual("!@#$%^&*()_+-={}|:\"<>?[]\\;',./'", cd(ce("!@#$%^&*()_+-={}|:\"<>?[]\\;',./'", 50), 50))
    def test_all_values_of_n(self):
        for n in range(-10000,10000):
            self.assertEqual("!@#$%^&*()_+-={}|:\"<>?[]\\;',./'The Quick Brown Fox Jumps Over The Lazy Dog", cd(ce("!@#$%^&*()_+-={}|:\"<>?[]\\;',./'The Quick Brown Fox Jumps Over The Lazy Dog", n), n))
