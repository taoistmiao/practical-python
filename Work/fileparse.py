# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename: str, select: list = [], types: list = [], has_headers: bool = True) -> "list[dict]":
    """
    Parse a csv file into a list of records
    """
    with open(filename, "rt") as f:
        rows = csv.reader(f)

        if has_headers:
            headers = next(rows)
            if select:
                indices = [headers.index(header) for header in select]
                headers = select

        records = []
        for row in rows:
            # skip blank lines
            if not row:
                continue
            if types:
                row = [func(val) for func, val in zip(types, row)]
            # exclude unselected entries
            if has_headers:
                row = [row[idx] for idx in indices]
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

    return records
