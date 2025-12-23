
# Architecture Overview: The Healer's Scribe

## Purpose
A modular, production-grade NLP platform for extracting insights from unstructured healer notes and medical texts.

## High-Level Architecture

- **src/**: Core application logic (NLP, API, services, utils)
- **config/**: Configuration, environment, and secrets management
- **static/**: Frontend assets (JS, CSS)
- **templates/**: Jinja2 HTML templates
- **scripts/**: Automation, utilities, and setup scripts
- **tests/**: Unit and integration tests
- **docs/**: Documentation and guides

## Key Modules
- **app.py**: Flask entrypoint, API, and web UI
- **src/core/**: NLP logic, entity extraction, sentiment, keyword analysis
- **src/services/**: Service layer for business logic
- **src/utils/**: Utility functions, logging, error handling

## Data Flow
1. User submits text or file via UI/API
2. Text is processed by NLP pipeline (modular, pluggable)
3. Results are returned as structured data and visualized

## Extensibility
- Add new NLP modules in `src/core/`
- Add new API endpoints in `src/`
- Add new tests in `tests/`

## Security
- No secrets in code; use `.env` and `config/`
- Input validation and error handling throughout

## Ownership
- See [CONTRIBUTING.md](CONTRIBUTING.md) for code ownership and review process
