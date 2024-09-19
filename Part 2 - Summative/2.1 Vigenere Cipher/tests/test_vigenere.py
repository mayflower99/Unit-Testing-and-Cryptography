from unittest import TestCase

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import vig_encode as ce
from main import vig_decode as cd


class TestInsertString(TestCase):
    def test_blank_equals_blank(self):
        self.assertEqual(ce("", "nj"), "")
    def test_one_letter_key(self):
        self.assertEqual("thequickbrownfoxjumpsoverthelazydog", cd(ce("thequickbrownfoxjumpsoverthelazydog", "0"), "0"))
    def test_long_key(self):
        self.assertEqual("thequickbrownfoxjumpsoverthelazydog", cd(ce("thequickbrownfoxjumpsoverthelazydog", "lidasf"), "lidasf"))
    def test_unusual_key(self):
        self.assertEqual("thequickbrownfoxjumpsoverthelazydog", cd(ce("thequickbrownfoxjumpsoverthelazydog", "{}{}:;."), "{}{}:;."))
    def test_spaces(self):
        self.assertEqual("the quick brown fox jumps over the lazy dog", cd(ce("the quick brown fox jumps over the lazy dog", "lidasf"), "lidasf"))
    def test_capitals(self):
        self.assertEqual("TheQuickBrownFoxJumpsOverTheLazyDog", cd(ce("TheQuickBrownFoxJumpsOverTheLazyDog", "lidasf"), "lidasf"))
    def test_special_charaters(self):
        self.assertEqual("!@#$%^&*()_+-={}|:\"<>?[]\\;',./'", cd(ce("!@#$%^&*()_+-={}|:\"<>?[]\\;',./'", "!@#$%^&*()_+-={}|:\"<>?[]\\;',./'"), "!@#$%^&*()_+-={}|:\"<>?[]\\;',./'"))
