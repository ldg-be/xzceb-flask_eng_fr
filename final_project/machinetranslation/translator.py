"""Module including all Watson Translation API interactions needed for this application"""

import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


load_dotenv()

def create_instance():
    """Creating the Watson Translation Instance"""
    apikey = os.environ['apikey']
    url = os.environ['url']
    print('part1')
    #Get the supported languages
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )

    language_translator.set_service_url(url)
    return language_translator

def get_languages():
    """Get the supported languages"""
    language_translator = create_instance()
    languages = language_translator.list_languages().get_result()
    print(json.dumps(languages, indent=2))

def englishToFrench(english_text):
    """Translate an english text to a french text."""
    if len(english_text)==0:
        print("Empty string")
        return ""
    language_translator = create_instance()
    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    return french_text['translations'][0]['translation']

def frenchToEnglish(french_text):
    """Translate a french text to an english text"""
    if len(french_text)==0:
        print("Empty string")
        return ""
    language_translator = create_instance()
    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()

    return english_text['translations'][0]['translation']
