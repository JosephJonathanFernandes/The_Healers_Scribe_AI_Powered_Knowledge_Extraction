# Rule-based NLP utilities for The Healer's Scribe (migrated from nlp.py)
import re
from typing import List, Dict, Tuple

POSITIVE_KEYWORDS = [
	"worked", "improved", "healed", "helped", "recovered", "good", "successful", "success", "well", "aided", "broke"
]
NEGATIVE_KEYWORDS = [
	"poor", "failed", "didn't", "did not", "no help", "no improvement", "worse", "ineffective", "not help", "bad", "worsened", "no improvement", "nothing changed"
]

def classify_sentiment(text: str) -> str:
	t = (text or '').lower()
	neg_hits = sum(1 for kw in NEGATIVE_KEYWORDS if kw in t)
	pos_hits = sum(1 for kw in POSITIVE_KEYWORDS if kw in t)
	if neg_hits > pos_hits and neg_hits > 0:
		return "negative"
	if pos_hits > neg_hits and pos_hits > 0:
		return "positive"
	if any(p in t for p in ['helped a bit', 'helped slightly', 'some improvement', 'helped a little']):
		return 'positive'
	if any(p in t for p in ["didn't help", "did not help", 'no improvement', 'no help']):
		return 'negative'
	return "neutral"

def extract_healer(text: str) -> str:
	m = re.search(r"(?:Healer|Dr\.?|Doctor|Elder|Brother|Sister|Sr|Mrs|Mr|Ms)\s+([A-Z][a-zA-Z'-.]+)", text)
	if m:
		return m.group(1)
	m2 = re.search(r"Healer\s+([A-Z])\b", text)
	if m2:
		return m2.group(1)
	m3 = re.search(r"^([A-Z][a-zA-Z'-.]+)\s+(used|applied|tried|administered|gave|brewed|attempted|prepared|made|created)", text)
	if m3:
		name = m3.group(1)
		if name.lower() not in ['the', 'a', 'an', 'and', 'but', 'or', 'for']:
			return name
	m4 = re.search(r"\b([A-Z][a-zA-Z]{2,})\s+(used|applied|tried|administered|gave|brewed|attempted|prepared)", text)
	if m4:
		name = m4.group(1)
		if name.lower() not in ['healer', 'doctor', 'elder', 'brother', 'sister', 'the', 'a', 'an']:
			return name
	return "Unknown"

def extract_cure_and_symptom(text: str) -> Tuple[str, str, str]:
	patterns = [
		r"used\s+([a-zA-Z0-9\s'-]+?)\s+for\s+([a-zA-Z0-9\s'-]+)[,\.-]?(.*)$",
		r"tried\s+([a-zA-Z0-9\s'-]+?)\s+for\s+([a-zA-Z0-9\s'-]+)[,\.-]?(.*)$",
		r"used\s+([a-zA-Z0-9\s'-]+?)\s+against\s+([a-zA-Z0-9\s'-]+)[,\.-]?(.*)$",
		r"applied\s+([a-zA-Z0-9\s'-]+?)\s+for\s+([a-zA-Z0-9\s'-]+)[,\.-]?(.*)$",
		r"administered\s+([a-zA-Z0-9\s'-]+?)\s+for\s+([a-zA-Z0-9\s'-]+)[,\.-]?(.*)$",
		r"gave\s+([a-zA-Z0-9\s'-]+?)\s+to\s+patients?\s+with\s+([a-zA-Z0-9\s'-]+)[,\.-]?(.*)$",
		r"used\s+a\s+poultice\s+of\s+([a-zA-Z0-9\s'-]+?)\s+for\s+([a-zA-Z0-9\s'-]+)[,\.-]?(.*)$",
	]
	for p in patterns:
		m = re.search(p, text, flags=re.IGNORECASE)
		if m:
			cure = m.group(1).strip()
			symptom = m.group(2).strip()
			outcome = (m.group(3) or "").strip()
			return cure, symptom, outcome
	return "", "", ""
