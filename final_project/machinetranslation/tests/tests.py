"""Import modulo unittest"""
import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    """Criando teste para atender os serviço do translator.py"""
    def test_translator_english_none(self):
        """Testar campo e nulo."""
        self.assertIsNone(english_to_french(None))
    def test_translator_english(self):
        """Testar campo não e nulo."""
        self.assertIsNotNone(english_to_french("Hello"))
    def test_translator_frenc_none(self):
        """Testar campo e nulo."""
        self.assertIsNotNone(french_to_english(None))
    def test_translator_frenc(self):
        """Testar campo não e nulo."""
        self.assertIsNotNone(french_to_english("Bonjour"))

unittest.main()
