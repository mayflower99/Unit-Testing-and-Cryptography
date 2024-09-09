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
        self.assertEqual(ce("thequickbrownfoxjumpsoverthelazydog", 0), cd(ce("thequickbrownfoxjumpsoverthelazydog", 0), 0))
    def test_n_equals_256(self):
        self.assertEqual(ce("thequickbrownfoxjumpsoverthelazydog", 256), cd(ce("thequickbrownfoxjumpsoverthelazydog", 0), 256))
    def test_n_equals_negitive(self):
        self.assertEqual(ce("thequickbrownfoxjumpsoverthelazydog", -256), cd(ce("thequickbrownfoxjumpsoverthelazydog", 0), -256))
    def test_spaces(self):
        self.assertEqual(ce("the quick brown fox jumps over the lazy dog", 256), cd(ce("the quick brown fox jumps over the lazy dog", 0), 256))
    def test_capitals(self):
        self.assertEqual(ce("thequickbrownfoxjumpsoverthelazydog", 256), cd(ce("thequickbrownfoxjumpsoverthelazydog", 0), 256))
    def test_special_charaters(self):
        self.assertEqual(ce("thequickbrownfoxjumpsoverthelazydog", 256), cd(ce("thequickbrownfoxjumpsoverthelazydog", 0), 256))