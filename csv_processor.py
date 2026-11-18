import csv
from pathlib import Path


def read_records(path: str | Path) -> list[dict[str, str]]:
    """Read a CSV with a header and return rows as dictionaries."""
    with Path(path).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def total_amount(records: list[dict[str, str]]) -> float:
    """Return the sum of the required numeric amount column."""
    return sum(float(row["amount"]) for row in records)
