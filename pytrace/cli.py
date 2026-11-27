"""Command-line interface for PyTrace."""

import argparse
from pathlib import Path

from pytrace import __version__
from pytrace.detectors import count_by_level, filter_by_level
from pytrace.exporters import export_csv, export_json
from pytrace.parsers import parse_file


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pytrace",
        description="Analyze plain-text application logs.",
    )
    parser.add_argument("--version", action="version", version=f"PyTrace {__version__}")
    subparsers = parser.add_subparsers(dest="command", required=True)

    analyze = subparsers.add_parser("analyze", help="Analyze a log file")
    analyze.add_argument("file", type=Path, help="Path to a text log file")
    analyze.add_argument("--level", help="Only show a severity level, e.g. ERROR")
    analyze.add_argument("--json", dest="json_path", type=Path, help="Write results to a JSON file")
    analyze.add_argument("--csv", dest="csv_path", type=Path, help="Write results to a CSV file")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.command == "analyze":
        if not args.file.is_file():
            print(f"Error: file not found: {args.file}")
            return 2

        records = parse_file(args.file)
        if args.level:
            records = filter_by_level(records, args.level)

        print(f"PyTrace analyzed: {args.file}")
        print(f"Records: {len(records)}")
        for level, count in count_by_level(records).items():
            print(f"  {level:<10} {count}")

        if args.json_path:
            export_json(records, args.json_path)
            print(f"JSON exported: {args.json_path}")
        if args.csv_path:
            export_csv(records, args.csv_path)
            print(f"CSV exported: {args.csv_path}")
        return 0

    return 0
