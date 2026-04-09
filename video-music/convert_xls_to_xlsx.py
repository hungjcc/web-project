#!/usr/bin/env python3
"""
Batch convert .xls files to .xlsx.

Usage examples:
  python3 convert_xls_to_xlsx.py ./videos
  python3 convert_xls_to_xlsx.py ./videos --recursive
  python3 convert_xls_to_xlsx.py ./videos --recursive --overwrite
  python3 convert_xls_to_xlsx.py ./videos --recursive --delete-source

Dependencies:
  pip install pandas xlrd openpyxl
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Batch convert .xls files to .xlsx in a folder."
    )
    parser.add_argument(
        "input_path",
        type=Path,
        help="Folder (or single .xls file) to convert.",
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="Scan subfolders recursively.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite target .xlsx if it already exists.",
    )
    parser.add_argument(
        "--delete-source",
        action="store_true",
        help="Delete source .xls after successful conversion.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what will be converted without writing files.",
    )
    return parser.parse_args()


def find_xls_files(input_path: Path, recursive: bool) -> list[Path]:
    if input_path.is_file():
        return [input_path] if input_path.suffix.lower() == ".xls" else []

    if not input_path.is_dir():
        return []

    pattern = "**/*.xls" if recursive else "*.xls"
    return sorted(p for p in input_path.glob(pattern) if p.is_file())


def convert_one_file(src: Path, overwrite: bool, dry_run: bool) -> tuple[bool, str]:
    dst = src.with_suffix(".xlsx")

    if dst.exists() and not overwrite:
        return False, f"SKIP: target exists -> {dst}"

    if dry_run:
        return True, f"DRY-RUN: {src} -> {dst}"

    try:
        import pandas as pd
    except ImportError:
        return (
            False,
            "ERROR: Missing dependency. Install with: pip install pandas xlrd openpyxl",
        )

    try:
        # Read all sheets from old .xls (xlrd engine)
        sheets = pd.read_excel(src, sheet_name=None, engine="xlrd")

        # Write to new .xlsx (openpyxl engine)
        with pd.ExcelWriter(dst, engine="openpyxl") as writer:
            for sheet_name, df in sheets.items():
                df.to_excel(writer, sheet_name=sheet_name, index=False)

        return True, f"OK: {src} -> {dst}"
    except Exception as exc:  # noqa: BLE001
        return False, f"ERROR: {src} ({exc})"


def main() -> int:
    args = parse_args()

    files = find_xls_files(args.input_path, args.recursive)
    if not files:
        print("No .xls files found.")
        return 1

    success_count = 0
    failed_count = 0

    for src in files:
        ok, message = convert_one_file(src, args.overwrite, args.dry_run)
        print(message)

        if ok:
            success_count += 1
            if args.delete_source and not args.dry_run:
                try:
                    src.unlink()
                    print(f"DELETED: {src}")
                except Exception as exc:  # noqa: BLE001
                    failed_count += 1
                    print(f"ERROR: failed to delete {src} ({exc})")
        else:
            failed_count += 1

    print("\nSummary")
    print(f"Total:   {len(files)}")
    print(f"Success: {success_count}")
    print(f"Failed:  {failed_count}")

    return 0 if failed_count == 0 else 2


if __name__ == "__main__":
    sys.exit(main())
