import json
from fuzzywuzzy import process
from utils import clean_text
from transliterate_hinglish import hinglish_to_hindi  # optional if you still want Hinglish support

# Load JSON
with open("hindi.json", "r", encoding="utf-8") as f:
    data_list = json.load(f)

# Convert list to dict
idiom_dict = {item["idiom"]: {"meaning_hindi": item.get("meaning_hindi", item["idiom"]),
                              "meaning_english": item.get("meaning_english", item.get("explanation", "No English meaning"))}
              for item in data_list}

# Function to explain idioms
def explain_idiom(user_input):
    idioms = list(idiom_dict.keys())
    match, score = process.extractOne(clean_text(user_input), idioms)
    
    if score > 70:
        meaning_hindi = idiom_dict[match]["meaning_hindi"]
        meaning_english = idiom_dict[match]["meaning_english"]
        return f"Hindi अर्थ: {meaning_hindi}\nEnglish Meaning: {meaning_english}"
    else:
        return "क्षमा करें, यह मुहावरा मेरे डेटाबेस में नहीं है।\nSorry, I don't know this idiom yet."

# -------------------------------
# 10 Test Cases (Hindi input)
# -------------------------------
test_cases = [
   "नज़रबंद करना",
    "धरना देना",
    "दीवारों के कान होना",
    "थक कर चूर होना",
    "तिनके का सहारा",
    "सांप भी मर जाए और लाठी भी न टूटे",
    "बंदर क्या जाने अदरक का",
    "छोटा मुँह बड़ी बात",
    "जख्म पर नमक छिड़कना",
    "टक्कर खाना"
]

print("🔹 Running 10 test cases in Hindi before starting chatbot:\n")
for i, test in enumerate(test_cases, 1):
    print(f"Test {i}: {test}")
    print("Bot:", explain_idiom(test))
    print("-" * 50)

# -------------------------------
# Chatbot loop
# -------------------------------
print("\n Hindi Idiom & Proverb Bilingual Bot")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("आप: ")
    if user_input.lower() == "exit":
        print("Bot: धन्यवाद! Keep learning!")
        break

    # Optionally, convert Hinglish to Hindi
    hindi_input = hinglish_to_hindi(user_input)
    print("Bot:", explain_idiom(hindi_input))
