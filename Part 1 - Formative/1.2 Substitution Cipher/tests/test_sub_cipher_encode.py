from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import sub_encode
from main import sub_decode

class TestInsertString(TestCase):
    def test_insert_string_two_words_lowercase(self):
        self.assertEqual(sub_encode("HELLOWORLD", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "mxtthahotu".upper())
    def test_spaces(self):
        self.assertEqual(sub_encode("H E L L O W O R L D", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "mxtthahotu".upper())
    def test_special_characters(self):
        self.assertEqual(sub_encode("HELL O W O R L D !@#$%^&*()_+-={}|[]\\:\";'<>?,./',\\", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "mxtthahotu".upper())
    def test_empty_string(self):
        self.assertEqual(sub_encode("", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "".upper())
    def test_different_alphabet(self):
        self.assertEqual(sub_encode("H E L L O W O R L D", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "HELLOWORLD".upper())
    def test_numbers(self):
        self.assertEqual(sub_encode("1234567890HELL O W O R L D !@#$%^&*()_+-={}|[]\\:\";'<>?,./',\\", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "mxtthahotu".upper())
    def test_subdecode(self):
        """if decorator works then tolerences should be the same as encode"""
        self.assertEqual(sub_decode("mxtthahotu", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "HELLOWORLD")