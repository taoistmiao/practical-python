# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename: str, select: list = []) -> "list[dict]":
    """
    Parse a csv file into a list of records
    """
    with open(filename, "rt") as f:
        rows = csv.reader(f)

        headers = next(rows)
        if select:
            indices = [headers.index(header) for header in select]
            headers = select

        records = []
        for row in rows:
            # skip blank lines
            if not row:
                continue
            # exclude unselected entries
            row = [row[idx] for idx in indices]
            record = dict(zip(headers, row))
            records.append(record)

    return records
