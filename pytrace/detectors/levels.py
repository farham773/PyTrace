"""Severity-level analysis."""

from collections import Counter
from collections.abc import Iterable

from pytrace.models import LogRecord


def count_by_level(records: Iterable[LogRecord]) -> dict[str, int]:
    """Count records by normalized severity level."""
    counts = Counter(record.level for record in records)
    return dict(sorted(counts.items()))


def filter_by_level(records: Iterable[LogRecord], level: str) -> list[LogRecord]:
    """Return records matching a severity level, case-insensitively."""
    normalized = level.upper()
    if normalized == "WARN":
        normalized = "WARNING"
    return [record for record in records if record.level == normalized]
