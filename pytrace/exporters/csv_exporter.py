"""CSV export support."""

import csv
from pathlib import Path
from collections.abc import Iterable

from pytrace.models import LogRecord

_FIELDS = ("timestamp", "level", "message", "source", "line_number")


def export_csv(records: Iterable[LogRecord], destination: str | Path) -> Path:
    """Write records as CSV and return the output path."""
    output = Path(destination)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=_FIELDS)
        writer.writeheader()
        writer.writerows(record.to_dict() for record in records)
    return output
