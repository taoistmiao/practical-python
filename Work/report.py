# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    """Read a portfolio into a list of tuples"""
    # portfolio = []

    # with open(filename, "rt") as f:
    #     rows = csv.reader(f)
    #     header = next(rows)
    #     for row in rows:
    #         holding = (row[0], int(row[1]), float(row[2]))
    #         portfolio.append(holding)
    portfolio = []

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            holding = {}
            holding["name"] = row[0]
            holding["shares"] = int(row[1])
            holding["price"] = float(row[2])
            portfolio.append(holding)

    return portfolio
