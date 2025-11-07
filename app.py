from flask import Flask, render_template, request, jsonify
import json
from fuzzywuzzy import process
from utils import clean_text
from transliterate_hinglish import hinglish_to_hindi



app = Flask(__name__)

# Load JSON data
with open("hindi.json", "r", encoding="utf-8") as f:
    data_list = json.load(f)

# Convert JSON to dictionary
idiom_dict = {
    item["idiom"]: {
        "meaning_hindi": item.get("meaning_hindi", item["idiom"]),
        "meaning_english": item.get("meaning_english", item.get("explanation", "No English meaning"))
    }
    for item in data_list
}

# Function to explain idiom
def explain_idiom(user_input):
    idioms = list(idiom_dict.keys())
    match, score = process.extractOne(clean_text(user_input), idioms)
    
    if score > 50:
        meaning_hindi = idiom_dict[match]["meaning_hindi"]
        meaning_english = idiom_dict[match]["meaning_english"]
        return f"Hindi अर्थ: {meaning_hindi}\nEnglish Meaning: {meaning_english}"
    else:
        return "क्षमा करें, यह मुहावरा मेरे डेटाबेस में नहीं है।\nSorry, I don't know this idiom yet."

# Load Hinglish alphabet mapping from JSON
with open("alphabet.json", "r", encoding="utf-8") as f:
    alphabet_map = json.load(f)
    
    
def hinglish_to_hindi(text):
    text = text.lower()
    result = ""
    i = 0
    while i < len(text):
        if i+2 < len(text) and text[i:i+3] in alphabet_map:
            result += alphabet_map[text[i:i+3]]
            i += 3
        elif i+1 < len(text) and text[i:i+2] in alphabet_map:
            result += alphabet_map[text[i:i+2]]
            i += 2
        elif text[i] in alphabet_map:
            result += alphabet_map[text[i]]
            i += 1
        else:
            result += text[i]
            i += 1
    return result
    

# -------------------------------
# Flask Routes
# -------------------------------

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    user_input = request.json["text"]
    hindi_input = hinglish_to_hindi(user_input)
    reply = explain_idiom(hindi_input)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
