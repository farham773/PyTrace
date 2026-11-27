"""Data models used throughout PyTrace."""

from dataclasses import asdict, dataclass


@dataclass(frozen=True, slots=True)
class LogRecord:
    """A single parsed log line."""

    timestamp: str | None
    level: str
    message: str
    source: str
    line_number: int

    def to_dict(self) -> dict[str, str | int | None]:
        """Return a JSON-friendly representation."""
        return asdict(self)
