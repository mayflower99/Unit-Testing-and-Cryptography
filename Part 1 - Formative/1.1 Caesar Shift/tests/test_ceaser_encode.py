from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import caesar_encode

class TestInsertString(TestCase):
    def test_n_equals_zero(self):
        self.assertEqual(caesar_encode("apple", 0), "apple")

    def test_empty_string(self):
        self.assertEqual(caesar_encode("", 12), 0)

    def test_n_is_greater_than_26(self):
        self.assertEqual(caesar_encode("apple", 100), "apple")

    def test_insert_string_empty_text(self):
        self.assertEqual(caesar_encode("", "orange"), "orange")

    def test_insert_string_whitespace(self):
        self.assertEqual(caesar_encode("  ", "orange"), " orange ")
