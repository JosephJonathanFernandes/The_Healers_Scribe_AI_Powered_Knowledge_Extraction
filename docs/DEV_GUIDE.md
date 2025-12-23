# Developer Experience Guide

## Linting & Formatting
- Use [Black](https://black.readthedocs.io/) for code formatting
- Use [Flake8](https://flake8.pycqa.org/) for linting
- Configuration in `.flake8`

## Pre-commit Hooks
- Install pre-commit: `pip install pre-commit`
- Run `pre-commit install` to enable hooks
- Hooks: Black, Flake8, trailing whitespace, end-of-file fixer

## CI/CD
- GitHub Actions pipeline runs on every push and PR
- Checks: lint (flake8), format (black), tests (pytest)
- See `.github/workflows/ci.yml`

## Coverage
- Target: 90%+
- Add tests for all new features and bugfixes
