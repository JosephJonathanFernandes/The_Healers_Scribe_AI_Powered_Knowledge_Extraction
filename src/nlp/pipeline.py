# src/nlp/pipeline.py
"""
NLP pipeline wrapper for The Healer's Scribe.
- Provides process_scrolls(text) and related utilities
- Uses advanced libraries if available, falls back to rule-based heuristics
"""
from typing import List, Dict, Any
import logging
import re

try:
    import spacy
    SPACY_AVAILABLE = True
except Exception:
    SPACY_AVAILABLE = False
else:
    try:
        _nlp = spacy.load("en_core_web_sm")
    except Exception:
        try:
            _nlp = spacy.load("en")
        except Exception:
            _nlp = None

try:
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    import nltk
    nltk.data.find('sentiment/vader_lexicon.zip')
    VADER_AVAILABLE = True
except Exception:
    VADER_AVAILABLE = False

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    SKLEARN_AVAILABLE = True
except Exception:
    SKLEARN_AVAILABLE = False

try:
    from transformers import pipeline as hf_pipeline
    TRANSFORMERS_AVAILABLE = True
except Exception:
    TRANSFORMERS_AVAILABLE = False

import pandas as pd
from .rule_based import parse_text

logger = logging.getLogger(__name__)

def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace('\r', ' ')).strip()

def extract_keywords_tfidf(texts: List[str], top_n: int = 10) -> List[str]:
    if not SKLEARN_AVAILABLE:
        words = ' '.join(texts).lower().split()
        freq = {}
        for w in words:
            if len(w) < 3:
                continue
            freq[w] = freq.get(w, 0) + 1
        return [k for k, _ in sorted(freq.items(), key=lambda x: -x[1])][:top_n]
    vectorizer = TfidfVectorizer(stop_words='english', max_features=2000)
    X = vectorizer.fit_transform(texts)
    scores = X.sum(axis=0).A1
    indices = scores.argsort()[-top_n:][::-1]
    return [vectorizer.get_feature_names_out()[i] for i in indices]

def extract_keywords_spacy(texts: List[str], top_n: int = 10) -> List[str]:
    if not SPACY_AVAILABLE or _nlp is None:
        return extract_keywords_tfidf(texts, top_n)
    doc = _nlp(' '.join(texts))
    candidates = set([chunk.text.lower() for chunk in doc.noun_chunks])
    candidates |= set([ent.text.lower() for ent in doc.ents])
    freq = {c: sum(c in t.lower() for t in texts) for c in candidates}
    return [k for k, _ in sorted(freq.items(), key=lambda x: -x[1])][:top_n]

def process_scrolls(text: str) -> Dict[str, Any]:
    records = parse_text(text)
    cures_pos_counts = {}
    cures_neg_counts = {}
    for r in records:
        cure = r.get('cure')
        sentiment = r.get('sentiment')
        if not cure:
            continue
        if sentiment == 'positive':
            cures_pos_counts[cure] = cures_pos_counts.get(cure, 0) + 1
        elif sentiment == 'negative':
            cures_neg_counts[cure] = cures_neg_counts.get(cure, 0) + 1
    all_texts = [r['raw'] for r in records]
    keywords = extract_keywords_spacy(all_texts) if SPACY_AVAILABLE else extract_keywords_tfidf(all_texts)
    summary = f"Processed {len(records)} records. Found {len(keywords)} keywords."
    return {
        'records': records,
        'cures_pos_counts': cures_pos_counts,
        'cures_neg_counts': cures_neg_counts,
        'keywords': keywords,
        'summary': summary
    }
