import pytest
from src.core import nlp

def test_classify_sentiment_positive():
    text = "The treatment worked very well and the patient improved."
    assert nlp.classify_sentiment(text) == "positive"

def test_classify_sentiment_negative():
    text = "The remedy did not help and the patient got worse."
    assert nlp.classify_sentiment(text) == "negative"

def test_extract_healer_title():
    text = "Healer Anna used garlic for infection."
    assert nlp.extract_healer(text) == "Anna"

def test_extract_cure_and_symptom():
    text = "Healer B used honey for cough, patients improved."
    cure, symptom, outcome = nlp.extract_cure_and_symptom(text)
    assert cure.lower() == "honey"
    assert symptom.lower() == "cough"
    assert "improved" in outcome
