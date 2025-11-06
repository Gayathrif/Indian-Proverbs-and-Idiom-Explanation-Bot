from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

def hinglish_to_hindi(text):
    """
    Convert Hinglish (Romanized Hindi) to Hindi (Devanagari)
    """
    try:
        return transliterate(text, sanscript.ITRANS, sanscript.DEVANAGARI)
    except Exception as e:
        print("Error in transliteration:", e)
        return text
