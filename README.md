# PyTrace

**A lightweight Python log analysis and intelligence toolkit.**

PyTrace is a small, dependency-free command-line tool for parsing plain-text application logs, summarizing severity levels, filtering records, and exporting results to JSON or CSV.

> Early development: PyTrace is an alpha project. Log parsing currently targets common timestamp-and-level text formats; it is not intended to replace production observability platforms.

## Features

- Parse common timestamped log lines and simple `LEVEL: message` lines.
- Preserve unrecognized non-empty lines as `UNKNOWN` records instead of silently discarding them.
- Summarize records by severity level.
- Filter results by severity.
- Export parsed records to JSON and CSV.
- Run tests with pytest and lint with Ruff.

## Requirements

- Python 3.10 or newer

## Installation

```bash
git clone https://github.com/farham773/PyTrace.git
cd PyTrace
python -m venv .venv
```

Activate the environment:

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux
source .venv/bin/activate
```

Install the project and development tools:

```bash
python -m pip install -e ".[dev]"
```

## Quick start

Analyze the included example:

```bash
pytrace analyze examples/sample.log
```

Filter errors and export the results:

```bash
pytrace analyze examples/sample.log --level ERROR --json reports/errors.json --csv reports/errors.csv
```

You can also run PyTrace without installing its command-line entry point:

```bash
python -m pytrace analyze examples/sample.log
```

## Development

Run the test suite:

```bash
pytest
```

Run lint checks:

```bash
ruff check .
```

## Project structure

```text
pytrace/
├── core/           # Application-level services
├── detectors/      # Severity analysis and filtering
├── exporters/      # JSON and CSV output
├── parsers/        # Text log parsing
├── cli.py          # Command-line interface
└── models.py       # Shared data models
tests/              # Automated tests
examples/           # Sample log files
```

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## License

PyTrace is licensed under the MIT License. See [LICENSE](LICENSE).
