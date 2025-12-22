
from src.nlp.pipeline import process_scrolls


def test_process_scrolls_sample_file():
def test_process_scrolls_basic():
    text = (
        "Healer A used garlic for infection, it worked well. "
        "Healer B used saltwater for fever - it did not help."
    )
    res = process_scrolls(text)
    assert 'records' in res
    assert isinstance(res['records'], list)
    pos = res.get('cures_pos_counts', {})
    neg = res.get('cures_neg_counts', {})
    assert any(v > 0 for v in pos.values())
    assert isinstance(res.get('keywords', []), list)

def test_process_scrolls_sample_file():
    import os
    sample_path = os.path.join(os.path.dirname(__file__), '..', 'sample_input.txt')
    with open(sample_path, 'r', encoding='utf-8') as f:
        s = f.read()
    res = process_scrolls(s)
    assert 'summary' in res
    assert len(res.get('keywords', [])) > 0
