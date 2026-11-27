from pytrace.parsers import parse_line


def test_parses_bracketed_level_and_timestamp():
    record = parse_line("2026-11-27 12:30:00 [ERROR] Connection failed")
    assert record is not None
    assert record.timestamp == "2026-11-27 12:30:00"
    assert record.level == "ERROR"
    assert record.message == "Connection failed"


def test_parses_simple_level_prefix():
    record = parse_line("WARN: Disk space is low")
    assert record is not None
    assert record.level == "WARNING"
    assert record.message == "Disk space is low"


def test_preserves_unknown_line():
    record = parse_line("Application started")
    assert record is not None
    assert record.level == "UNKNOWN"
    assert record.message == "Application started"


def test_ignores_blank_line():
    assert parse_line("   \n") is None
