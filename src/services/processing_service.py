# src/services/processing_service.py
"""
Service layer for NLP processing and business logic.
"""
from src.nlp.pipeline import process_scrolls

def analyze_text(text: str):
    return process_scrolls(text)
