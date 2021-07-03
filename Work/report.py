# report.py
#
# Exercise 2.4
import csv
from os import sep

def read_portfolio(filename):
    """Read a portfolio into a list of (tuples) dictionaries (name, shares, price)"""
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
            record = dict(zip(header, row))
            holding = {}
            holding["name"] = record["name"]
            holding["shares"] = int(record["shares"])
            holding["price"] = float(record["price"])
            portfolio.append(holding)

    return portfolio

def read_prices(filename):
    """Read prices into dictionary with stock names as keys"""
    prices = {}

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        try:
            for row in rows:
                prices[row[0]] = float(row[1])
        except:
            pass

    return prices

def make_report(portfolio: "list[dict]", prices: dict) -> "list[tuple]":
    report_list = []
    for stock in portfolio:
        report = (
            stock["name"], 
            stock["shares"], 
            prices[stock["name"]], 
            prices[stock["name"]]-stock["price"]
            )
        report_list.append(report)

    return report_list

def show_report():
    portfolio = read_portfolio("Data/portfolio.csv")
    prices = read_prices("Data/prices.csv")
    report = make_report(portfolio, prices)
    headers = ("Name", "Shares", "Price", "Change")
    print("%10s %10s %10s %10s" % headers)
    separator = "-" * 10
    print(f"{separator} {separator} {separator} {separator}")
    for name, shares, price, change in report:
        print("{:>10s} {:>10d} {:>10s} {:>10s}".format(name, shares, f"${price:.2f}", f"${change:.2f}"))

show_report()
