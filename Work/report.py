#!/usr/bin/env python3
# report.py
#
# Exercise 2.4
import csv
from os import sep
from fileparse import parse_csv
import stock as stk
import tableformat

def read_portfolio(filename):
    """Read a portfolio into a list dictionaries (name, shares, price)"""
    with open(filename, "rt") as f:
        portfolio_dict = parse_csv(f, select=['name','shares','price'], types=[str,int,float])
        portfolio = [stk.Stock(d['name'], d['shares'], d['price']) for d in portfolio_dict]

    return portfolio

def read_prices(filename):
    """Read prices into dictionary with stock names as keys"""
    with open(filename, "rt") as f:
        prices = parse_csv(f, types=[str, float], has_headers=False)

    return dict(prices)

def make_report(portfolio: "list[stk.Stock]", prices: dict) -> "list[tuple]":
    report_list = []
    for stock in portfolio:
        report = (
            stock.name,
            stock.shares,
            prices[stock.name],
            prices[stock.name]-stock.price
            )
        report_list.append(report)

    return report_list

def show_report(portfolio_file, prices_file, format):
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)
    report = make_report(portfolio, prices)
    formatter = tableformat.create_formatter(format)

    headers = ["Name", "Shares", "Price", "Change"]
    formatter.headings(headers)
    for name, shares, price, change in report:
        row_data = [name, str(shares), f"${price:.2f}", f"${change:.2f}"]
        formatter.row(row_data)


def main(args: list):
    if len(args) != 4:
        raise SystemExit('Usage: %s portfile pricefile format' % args[0])
    show_report(args[1], args[2], args[3])

if __name__ == "__main__":
    import sys
    main(sys.argv)
