"""Import modulo unittest"""
import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    """Criando teste para atender os serviço do translator.py"""
    def test_translator_english_none(self):
        """Testar campo e diferente."""
        self.assertNotEqual(english_to_french("Hello"), "Hello")
    def test_translator_english(self):
        """Testar campo não e nulo."""
        self.assertEqual(english_to_french("Hello"), "Hello")
    def test_translator_frenc_none(self):
        """Testar campo e diferente."""
        self.assertNotEqual(french_to_english("Bonjour"), "bonjour")
    def test_translator_frenc(self):
        """Testar campo não e nulo."""
        self.assertEqual(french_to_english("Bonjour"), "Bonjour")

unittest.main()
