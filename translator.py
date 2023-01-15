# translate.py - takes given text and, using the translators library, fetches a translation of the sentence.
from translate import Translator

def translateText(text : str, language : str = "zh") -> str:
    """
    Takes an input string and outputs its translated version in the specified language.
    :param text: Phrase to be translated (string).
    :param language: Two letter string corresponding to language to translate to (defaults to simplified chinese).
    """
    print(text, language)
    translator = Translator(to_lang = language)
    translation = translator.translate(text)
    
    return translation
