from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

def hinglish_to_hindi(text):
    """
    Convert Hinglish (Romanized Hindi) to Hindi (Devanagari) with normalization.
    Handles informal spelling variations better.
    """
    try:
        # Transliterate using Harvard-Kyoto scheme (more flexible than ITRANS)
        hindi_text = transliterate(text, sanscript.HK, sanscript.DEVANAGARI)
        # Normalize: lowercase, strip, remove extra spaces
        hindi_text = hindi_text.strip().replace("  ", " ").lower()
        return hindi_text
    except Exception as e:
        print("Error in transliteration:", e)
        return text.strip().lower()
