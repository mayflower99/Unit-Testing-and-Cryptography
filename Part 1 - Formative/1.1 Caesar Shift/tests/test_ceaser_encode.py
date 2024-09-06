from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import caesar_encode

def int_array_from_char(string):
    return [ord(x) for x in string]
def int_array_from_string(string):
    return [int(x) for x in string.split()]
class TestInsertString(TestCase):
    def test_blank_equals_blank(self):
        self.assertEqual(caesar_encode("", n), "")
    def test_n_equals_0(self):
        self.assertEqual(caesar_encode("thequickbrownfoxjumpsoverthelazydog", 0), "thequickbrownfoxjumpsoverthelazydog")
    def test_n_equals_256(self):
        self.assertEqual(caesar_encode("thequickbrownfoxjumpsoverthelazydog", 256), "thequickbrownfoxjumpsoverthelazydog")
    def test_n_equals_negitive(self):
        self.assertEqual(int_array_from_char(caesar_encode("thequickbrownfoxjumpsoverthelazydog", -50)), int_array_from_string("12 0 125 9 13 1 123 3 122 10 7 15 6 126 7 16 2 13 5 8 11 7 14 125 10 12 0 125 4 121 18 17 124 7 127"))
    def test_spaces(self):
        self.assertEqual(int_array_from_char(caesar_encode("the quick brown fox jumps over the lazy dog", 1)), int_array_from_string("117 105 102 33 114 118 106 100 108 33 99 115 112 120 111 33 103 112 121 33 107 118 110 113 116 33 112 119 102 115 33 117 105 102 33 109 98 123 122 33 101 112 104"))
    def test_capitals(self):
        self.assertEqual(int_array_from_char(caesar_encode("TheQuickBrownFoxJumpsOverTheLazyDog", 1)), int_array_from_string("85 105 102 82 118 106 100 108 67 115 112 120 111 71 112 121 75 118 110 113 116 80 119 102 115 85 105 102 77 98 123 122 69 112 104"))
    def test_special_charaters(self):
        self.assertEqual(int_array_from_char(caesar_encode("TheQuickBrownFoxJumpsOverTheLazyDog", 1)), int_array_from_string("85 105 102 82 118 106 100 108 67 115 112 120 111 71 112 121 75 118 110 113 116 80 119 102 115 85 105 102 77 98 123 122 69 112 104"))