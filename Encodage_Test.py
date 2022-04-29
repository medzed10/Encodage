import unittest
from Solution.Ascii import Ascii
from Solution.Utf16 import Utf16
from Solution.Utf32 import Utf32
from Solution.Utf8 import Utf8


class EncodageTest(unittest.TestCase):

    def test_create_Ascii(self):
        ascii = Ascii("coucou")
        assert ascii.chaine=="coucou"

    def test_taille_memoire_Ascii(self):
        ascii = Ascii("coucou")
        self.assertTrue(ascii.taille_memoire()==6)

    def test_create_Utf8(self):
        utf8 = Utf8("coucou")
        assert utf8.chaine=="coucou"

    def test_taille_memoire_Utf8(self):
        utf8 = Utf8("coucou")
        self.assertTrue(utf8.taille_memoire()==6)

    def test_create_Utf16(self):
        utf16 = Utf16("coucou")
        assert utf16.chaine=="coucou"

    def test_taille_memoire_Utf16(self):
        utf16 = Utf16("coucou")
        self.assertTrue(utf16.taille_memoire()==14)

    def test_create_Utf32(self):
        utf32= Utf32("coucou")
        assert utf32.chaine=="coucou"

    def test_taille_memoire_Utf32(self):
        utf32= Utf32("coucou")
        self.assertTrue(utf32.taille_memoire()==28)

