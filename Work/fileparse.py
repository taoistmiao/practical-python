# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename: str, select: list = [], types: list = [], has_headers: bool = True, delimiter: str = ",", silence_errors: bool = False) -> "list[dict]":
    """
    Parse a csv file into a list of records
    """
    if types and not has_headers:
        raise RuntimeError("select argument requires column headers")
    with open(filename, "rt") as f:
        rows = csv.reader(f, delimiter=delimiter)

        if has_headers:
            headers = next(rows)
            if select:
                indices = [headers.index(header) for header in select]
                headers = select

        records = []
        for line, row in enumerate(rows, start=1):
            # skip blank lines
            if not row:
                continue
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        print(f"Row {line}: Couldn't convert {row}")
                        print(f"Row {line}: Reason {e}")
                    continue

            # exclude unselected entries
            if has_headers:
                if select:
                    row = [row[idx] for idx in indices]
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

    return records
