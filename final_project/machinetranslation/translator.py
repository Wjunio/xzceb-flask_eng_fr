"""imports"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

"""Método para traduzir do ingles para o frances e frances para ingles"""
def english_to_french(english_text):
    """Inicializando variavel"""
    french_text = None
    if english_text is not None:
        authenticator = IAMAuthenticator(apikey)
        language_translator = LanguageTranslatorV3(
            version='2023-01-22',
            authenticator=authenticator
        )
        language_translator.set_service_url(url)
        translation = language_translator.translate(text=english_text, model_id='en-fr')
        translation.get_result()
        french_text = json.dumps(translation, indent=2, ensure_ascii=False)
    return french_text

def french_to_english(french_text):
    """Inicializando variavel"""
    english_text = None
    if french_text is not None:
        authenticator = IAMAuthenticator(apikey)
        language_translator = LanguageTranslatorV3(
            version='2023-01-22',
            authenticator=authenticator
        )
        language_translator.set_service_url(url)
        translation = language_translator.translate( text=french_text, model_id='fr-CA-en')
        translation.get_result()
        english_text = json.dumps(translation, indent=1, ensure_ascii=False)
    return english_text
