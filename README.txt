Project Title: Hindi Idiom & Proverb Bilingual Bot

Objective:
Explain Hindi idioms and proverbs in both Hindi and English using Hinglish input.

Tools & Libraries:
Python, fuzzywuzzy, python-Levenshtein, pandas, indic-transliteration

Dataset:
- Source: Kaggle - Multilingual Idioms & Proverbs (Indian)
- Filtered for Hindi language
- Stored in hindi.json

Methodology:
1. Accept user input in Hinglish.
2. Convert Hinglish to Hindi script.
3. Use fuzzy matching to find the closest idiom in the dataset.
4. Display meanings in Hindi and English.
5. Repeat until user types 'exit'.

Sample Run:
आप: nak katna
Bot: Hindi अर्थ: नाक कटना
English Meaning: To be embarrassed or lose respect
