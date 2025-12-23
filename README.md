# The Healer's Scribe

**A modular, production-grade NLP platform for extracting insights from unstructured healer notes and medical texts.**

---

## 🚩 Problem
Healers and researchers face scattered, unstructured records. Extracting actionable insights is slow and error-prone.

## 💡 Solution
The Healer's Scribe uses modern NLP to:
- Extract entities (treatments, symptoms, outcomes)
- Classify effectiveness and sentiment
- Visualize patterns and trends
- Provide a secure, extensible API and UI

## 🏗️ Architecture
- Modular Python backend (see [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md))
- Flask API and web UI
- Config-driven, secure by default
- Extensible NLP pipeline (spaCy, NLTK, scikit-learn, transformers)

## 🛠️ Tech Stack
- Python 3.8+
- Flask
- spaCy, NLTK, scikit-learn, transformers (optional)
- Plotly (visualization)
- Docker-ready

## 📦 Repository Structure

```
src/            # Core logic (NLP, API, services, utils)
config/         # Configuration and environment
static/         # Frontend assets (JS, CSS)
templates/      # Jinja2 HTML templates
scripts/        # Automation and utilities
tests/          # Unit and integration tests
docs/           # Documentation and guides
sample_data/    # Example input data
requirements.txt
.env.example    # Environment variable template
app.py          # Entrypoint (Flask app)
```

## 🚀 Getting Started

1. **Clone and set up environment:**
   ```sh
   git clone <repo-url>
   cd The_Healers_Scribe_AI_Powered_Knowledge_Extraction
   python -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   pip install -r requirements.txt
   cp .env.example .env
   # Edit .env as needed
   ```
2. **Run the app:**
   ```sh
   flask run
   # or python app.py
   ```
3. **Visit:** [http://localhost:5000](http://localhost:5000)

## 🧪 Testing
- Tests in `tests/` (unit & integration)
- Run: `pytest`
- Coverage goal: 90%+

## 🧹 Linting & Formatting
- Use `black` for formatting
- Use `flake8` for linting
- Pre-commit hooks recommended (see below)

## 🔒 Security
- No secrets in code; use `.env` and `config/`
- Input validation and error handling throughout
- See [SECURITY.md](SECURITY.md)

## 🤝 Contributing
- See [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)

## 🛡️ API Usage

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

## 🧬 NLP Pipeline Details
See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for full details.

## 📝 Documentation
- [ARCHITECTURE.md](docs/ARCHITECTURE.md): System design and data flow
- [CONTRIBUTING.md](docs/CONTRIBUTING.md): How to contribute
- [SECURITY.md](SECURITY.md): Security policy
- [CHANGELOG.md](CHANGELOG.md): Release notes

## 🏆 Judging Criteria Alignment
| Criterion | Implementation |
|-----------|----------------|
| **Innovation (40%)** | Automatic structuring of unstructured data; entity extraction; multi-class classification; creative visualizations |
| **AI Implementation (30%)** | NER, text classification, sentiment analysis, topic modeling; uses spaCy, sklearn, VADER, Transformers |
| **MVP (20%)** | End-to-end working prototype: paste text → get dashboard with actionable insights; API + web UI |

## 📈 Future Enhancements
- [ ] Fine-tuned NER models for medical domain
- [ ] Multi-language support
- [ ] Time-series analysis for cure effectiveness trends
- [ ] RAG-based chatbot for querying extracted knowledge
- [ ] SQLite persistence for historical tracking

## 📄 License
MIT License — feel free to use for hackathons, prototypes, or research.

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

## Contact & Project History

This project was built for "The Knowledge of the Healers" AI challenge.

- Repository: `temporal_forge`
- Owner: JosephJonathanFernandes
- Contact: [Open an Issue](https://github.com/JosephJonathanFernandes/temporal_forge/issues) or see repository profile

### Project Milestones
- Initial design and modularization of Flask app and NLP pipeline
- Implementation of core NLP (entity extraction, sentiment, topic modeling)
- Secure configuration and environment management
- Professional documentation, testing, and CI/CD integration
- Modern UI/UX with accessible templates and static assets

### Key Files & Structure
- `app.py` — Flask entrypoint and API
- `src/core/` — Modular NLP logic (entity extraction, sentiment, topics)
- `src/services/` — Service layer for business logic
- `src/utils/` — Logging and utility functions
- `config/` — Environment and settings
- `templates/` — Jinja2 HTML templates
- `static/` — CSS and JS assets
- `tests/` — Unit and integration tests
- `requirements.txt` — Python dependencies

For packaging, use the provided `package_project.ps1` script or standard zip tools.
