import csv
import json

from pytrace.detectors import count_by_level, filter_by_level
from pytrace.exporters import export_csv, export_json
from pytrace.models import LogRecord


def sample_records():
    return [
        LogRecord("2026-11-27 10:00:00", "INFO", "Started", "app.log", 1),
        LogRecord("2026-11-27 10:01:00", "ERROR", "Failed", "app.log", 2),
        LogRecord(None, "ERROR", "Timeout", "app.log", 3),
    ]


def test_count_and_filter_levels():
    records = sample_records()
    assert count_by_level(records) == {"ERROR": 2, "INFO": 1}
    assert len(filter_by_level(records, "error")) == 2


def test_json_export(tmp_path):
    output = export_json(sample_records(), tmp_path / "nested" / "logs.json")
    data = json.loads(output.read_text(encoding="utf-8"))
    assert len(data) == 3
    assert data[1]["level"] == "ERROR"


def test_csv_export(tmp_path):
    output = export_csv(sample_records(), tmp_path / "logs.csv")
    with output.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 3
    assert rows[0]["level"] == "INFO"
