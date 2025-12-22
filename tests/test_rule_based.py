# tests/test_rule_based.py
"""
Unit tests for rule-based NLP utilities.
"""
import pytest
from src.nlp.rule_based import classify_sentiment, parse_text

def test_classify_sentiment_positive():
    assert classify_sentiment("it worked well") == "positive"
    assert classify_sentiment("patients healed quickly") == "positive"
    assert classify_sentiment("it helped a bit") == "positive"

def test_classify_sentiment_negative():
    assert classify_sentiment("results were poor") == "negative"
    assert classify_sentiment("it didn't help") == "negative"
    assert classify_sentiment("no improvement observed") == "negative"

def test_classify_sentiment_neutral():
    assert classify_sentiment("used honey for cough") == "neutral"
    assert classify_sentiment("applied crushed mint") == "neutral"

def test_parse_text_extracts_records():
    text = "Healer A used garlic for infection, it worked well."
    records = parse_text(text)
    assert isinstance(records, list)
    assert len(records) == 1
    rec = records[0]
    assert rec["healer"] == "A"
    assert rec["cure"] == "garlic"
    assert rec["symptom"] == "infection"
    assert rec["sentiment"] == "positive"
