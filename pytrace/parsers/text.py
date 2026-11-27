"""Parser for common plain-text application log formats."""

from pathlib import Path
import re
from collections.abc import Iterator

from pytrace.models import LogRecord

_LEVEL = r"DEBUG|INFO|WARNING|WARN|ERROR|CRITICAL|FATAL"
_PATTERNS = (
    re.compile(
        rf"^(?P<timestamp>\d{{4}}-\d{{2}}-\d{{2}}[T ][0-9:.+-]+Z?)\s+\[(?P<level>{_LEVEL})\]\s*(?P<message>.*)$",
        re.IGNORECASE,
    ),
    re.compile(
        rf"^(?P<timestamp>\d{{4}}-\d{{2}}-\d{{2}}[ T][0-9:.+-]+)\s+(?P<level>{_LEVEL})\s+(?P<message>.*)$",
        re.IGNORECASE,
    ),
    re.compile(rf"^(?P<level>{_LEVEL})\s*:\s*(?P<message>.*)$", re.IGNORECASE),
)


def parse_line(line: str, *, source: str = "<string>", line_number: int = 1) -> LogRecord | None:
    """Parse one line. Blank lines are ignored; unknown lines are preserved."""
    cleaned = line.rstrip("\r\n")
    if not cleaned.strip():
        return None

    for pattern in _PATTERNS:
        match = pattern.match(cleaned.strip())
        if match:
            values = match.groupdict()
            return LogRecord(
                timestamp=values.get("timestamp"),
                level=(values["level"] or "UNKNOWN").upper().replace("WARN", "WARNING"),
                message=values.get("message", "").strip(),
                source=source,
                line_number=line_number,
            )

    return LogRecord(
        timestamp=None,
        level="UNKNOWN",
        message=cleaned.strip(),
        source=source,
        line_number=line_number,
    )


def parse_file(path: str | Path) -> list[LogRecord]:
    """Read and parse a UTF-8 text log file."""
    file_path = Path(path)
    records: list[LogRecord] = []
    with file_path.open("r", encoding="utf-8", errors="replace") as handle:
        for number, line in enumerate(handle, start=1):
            record = parse_line(line, source=str(file_path), line_number=number)
            if record is not None:
                records.append(record)
    return records
