# The Healer's Scribe

A modular, production-grade NLP platform for extracting insights from unstructured healer notes and medical texts.

## Problem Statement
Healers and researchers face scattered, unstructured records. Extracting actionable insights is slow and error-prone.

## Solution
The Healer's Scribe uses modern NLP to:
- Extract entities (treatments, symptoms, outcomes)
- Classify effectiveness and sentiment
- Visualize patterns and trends
- Provide a secure, extensible API and UI

## Architecture
- Modular Python backend (see docs/ARCHITECTURE.md)
- Flask API and web UI
- Config-driven, secure by default
- Extensible NLP pipeline (spaCy, NLTK, scikit-learn, transformers)

## Tech Stack
- Python 3.8+
- Flask
- spaCy, NLTK, scikit-learn, transformers (optional)
- Plotly (visualization)
- Docker-ready

## Setup
1. Clone the repo and create a virtual environment:
  ```sh
  python -m venv .venv
  source .venv/bin/activate  # or .venv\Scripts\activate on Windows
  pip install -r requirements.txt
  cp .env.example .env
  # Edit .env as needed
  ```
2. Run the app:
  ```sh
  flask run
  # or python app.py
  ```
3. Sample input data is in `sample_data/sample_input.txt`

## Testing
- Tests in `tests/` (unit & integration)
- Run: `pytest`
- Coverage goal: 90%+

## Linting & Formatting
- Use `black` for formatting
- Use `flake8` for linting
- Pre-commit hooks recommended (see below)

## CI/CD
- GitHub Actions pipeline recommended (see below)

## Security
- No secrets in code; use `.env` and `config/`
- Input validation and error handling throughout
- See SECURITY.md

## Contributing
- See docs/CONTRIBUTING.md


## Upcoming Features
- **Retrieval-Augmented Generation (RAG):**
  - Planned integration for advanced Q&A and knowledge retrieval from healer notes and medical texts.
  - Not yet implemented, but designed for future extensibility.

## Project Context
- This project was developed as part of a competition challenge to demonstrate modular NLP engineering, security, and open-source best practices.
pip install spacy nltk transformers torch
python -m spacy download en_core_web_sm
python -c "import nltk; nltk.download('vader_lexicon')"
```

### 2. Run the Application

```powershell
# Set Flask app
$env:FLASK_APP = 'app.py'

# Run in development mode
flask run

# Or run directly
python app.py
```

Visit: `http://localhost:5000`

---

## API Usage

### Health Check
```bash
curl http://localhost:5000/health
```

### Process Text (JSON API)
```bash
curl -X POST http://localhost:5000/api/process \
  -H "Content-Type: application/json" \
  -d '{"text": "Healer Anna used garlic for infections — patients healed quickly."}'
```

**Response includes:**
- `records`: Parsed structured records with healer, cure, symptom, outcome, sentiment, classification
- `cures_pos_counts`: Positive mentions per cure
- `cures_neg_counts`: Negative mentions per cure
- `keywords`: Top extracted keywords
- `summary`: Auto-generated insight summary
- `entities`: Extracted healers, treatments, symptoms, diseases
- `topics`: Top themes from the text
- `sentiment_scores`: VADER sentiment scores

---

## Project Structure

```
temporal_forge/
├── app.py                  # Flask application with web UI and API
├── nlp.py                  # Rule-based NLP parser
├── models/
│   └── nlp_pipeline.py    # Advanced NLP pipeline with NER, classification, topic modeling
├── templates/              # HTML templates
│   ├── landing.html
│   ├── index.html
│   └── result.html
├── static/                 # CSS and JavaScript
│   ├── styles.css
│   ├── ui.js
│   ├── chat.js
│   └── chart.js
├── tests/
│   └── test_nlp.py        # Pytest unit tests
├── scripts/
│   └── run_nlp_test.py    # Test script for NLP modules
├── sample_input.txt        # Example input data
├── requirements.txt        # Python dependencies
└── .env.example           # Environment configuration template
```

---

## Testing

```powershell
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_nlp.py
```

---

## NLP Pipeline Details

### 1. Text Preprocessing
- Sentence segmentation
- Normalization and cleaning
- Multi-format input support (PDF, JSON, TXT)

### 2. Entity Extraction
Extracts:
- **Healers**: Person names, titles (Healer, Dr., Elder)
- **Treatments**: Herbs, remedies, procedures
- **Symptoms**: Fever, cough, infection, etc.
- **Diseases**: Identified conditions

### 3. Classification
Labels each record as:
- `effective` — Treatment worked
- `failure` — Treatment failed
- `complaint` — Patient complaint
- `praise` — Positive feedback
- `neutral` — No clear outcome

### 4. Sentiment Analysis
- Uses VADER when available
- Falls back to keyword-based heuristics
- Scores range from -1 (negative) to +1 (positive)

### 5. Topic Modeling
- TF-IDF-based keyword extraction
- Identifies common themes and patterns
- Surfaces most discussed cures and failure points

---

## Example Workflow

1. **Input**: Paste or upload unstructured healer notes
2. **Processing**: NLP pipeline extracts entities, classifies records, analyzes sentiment
3. **Output**: Dashboard shows:
   - Top 5 most effective cures
   - Most common failures
   - Interactive charts with effectiveness percentages
   - Downloadable reports (CSV/JSON/PDF)

---

## Advanced Configuration

Copy `.env.example` to `.env` and customize:

```bash
FLASK_ENV=production
PORT=8080
# API_KEY=your_secret_key  # Uncomment for API authentication
# SENTRY_DSN=your_dsn      # Uncomment for error tracking
```

---

## Development Tips

### Add New NLP Features

Edit `models/nlp_pipeline.py`:
- `extract_entities()` — Add new entity types
- `classify_record()` — Refine classification rules
- `topics_from_texts()` — Enhance topic extraction

### Improve Parsing

Edit `nlp.py`:
- Update `POSITIVE_KEYWORDS` and `NEGATIVE_KEYWORDS`
- Add new regex patterns to `extract_cure_and_symptom()`
- Enhance `extract_healer()` for more title formats

---

## Judging Criteria Alignment

| Criterion | Implementation |
|-----------|----------------|
| **Innovation (40%)** | Automatic structuring of unstructured data; entity extraction; multi-class classification; creative visualizations with effectiveness percentages |
| **AI Implementation (30%)** | NER, text classification, sentiment analysis, topic modeling; uses spaCy, sklearn, VADER, Transformers |
| **MVP (20%)** | End-to-end working prototype: paste text → get dashboard with actionable insights; API + web UI |

---

## Future Enhancements

- [ ] Fine-tuned NER models for medical domain
- [ ] Multi-language support
- [ ] Time-series analysis for cure effectiveness trends
- [ ] RAG-based chatbot for querying extracted knowledge
- [ ] SQLite persistence for historical tracking

---

## License

MIT License — feel free to use for hackathons, prototypes, or research.

---

## Contact

Built for "The Knowledge of the Healers" AI challenge.  
Repository: `temporal_forge`  
Owner: JosephJonathanFernandes
- Create Flask app, templates and static files.

Hour 2 — Input/output pages
- Build `index.html` and `result.html` pages to accept input and show results.

Hour 3–4 — AI core
- Implement `models/nlp_pipeline.py` (NER, sentiment, TF-IDF, summarization fallbacks).

Hour 5 — Connect Flask
- Wire routes to processing and add download endpoints (CSV/JSON/TXT/PDF).

Hour 6 — Polish and present
- Add charts, styling, and package the folder for deployment or demo.

Files included in this repo
- `app.py` — Flask server and routes (index, downloads)
- `models/nlp_pipeline.py` — processing wrapper (uses heuristics or optional heavy libs)
- `nlp.py` — simple rule-based parser used as fallback
- `templates/` — `index.html` (main UI) and `result.html` (result layout)
- `static/` — `styles.css` and `chart.js` for UI polish
- `requirements.txt` — minimal deps; extras optional for better NLP

Want a ready package? Run the `package_project.ps1` script (added to repo) or use the PowerShell compress command to build a zip of the project.
