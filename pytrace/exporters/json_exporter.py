"""JSON export support."""

import json
from pathlib import Path
from collections.abc import Iterable

from pytrace.models import LogRecord


def export_json(records: Iterable[LogRecord], destination: str | Path) -> Path:
    """Write records as a UTF-8 JSON array and return the output path."""
    output = Path(destination)
    output.parent.mkdir(parents=True, exist_ok=True)
    payload = [record.to_dict() for record in records]
    output.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return output
