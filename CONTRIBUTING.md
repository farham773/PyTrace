# Contributing to PyTrace

Thanks for considering a contribution!

## Development setup

1. Fork the repository and clone your fork.
2. Create and activate a Python 3.10+ virtual environment.
3. Install development dependencies with `python -m pip install -e ".[dev]"`.
4. Create a focused branch for your change.

## Before opening a pull request

Run the checks:

```bash
pytest
ruff check .
```

Please include tests for bug fixes and new behavior. Keep pull requests focused, describe the user-facing change, and avoid unrelated formatting changes.

## Pull request process

- Open an issue first for substantial changes.
- Target the repository's `dev` branch when one exists; otherwise target its default branch.
- Explain the problem, the solution, and how you tested it.
- Be respectful and constructive during review.
