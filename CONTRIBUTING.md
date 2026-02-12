# Contributing to Guardrail

## Getting Started

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Write tests for new functionality
5. Run tests: `pytest tests/`
6. Commit with clear messages: `git commit -m "add feature: description"`
7. Push and create a pull request

## Code Style

- Use Black for formatting: `black .`
- Use flake8 for linting: `flake8 .`
- Follow PEP 8 conventions
- Add docstrings to functions and classes

## Testing Requirements

- All new features must include unit tests
- Maintain >80% code coverage
- Run: `pytest --cov=guardrail tests/`

## Commit Message Format

```
<type>: <subject>

<body>

<footer>
```

Types: feat, fix, docs, style, refactor, test, chore

## Reporting Issues

Include:
- Python version
- OS and environment
- Steps to reproduce
- Expected vs actual behavior
- Relevant logs or stack traces

## Feature Requests

Describe:
- Problem being solved
- Proposed solution
- Alternative approaches considered
- Additional context

## Questions?

Open a discussion or reach out to the maintainers.

