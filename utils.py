import re

def clean_text(text):
    text = text.strip()
    text = re.sub(r"[^\w\s\u0900-\u097F]", "", text)  # Keep Hindi letters
    return text
