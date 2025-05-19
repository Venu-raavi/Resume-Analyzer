import spacy
import re

nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def tokenize(text):
    return [token.lemma_.lower() for token in nlp(text) if not token.is_stop and token.is_alpha]
