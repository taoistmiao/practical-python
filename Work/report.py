# report.py
#
# Exercise 2.4
import csv
from os import sep
from fileparse import parse_csv

def read_portfolio(filename):
    """Read a portfolio into a list dictionaries (name, shares, price)"""
    portfolio = parse_csv(filename, select=['name','shares','price'], types=[str,int,float])

    return portfolio

def read_prices(filename):
    """Read prices into dictionary with stock names as keys"""
    prices = parse_csv(filename, types=[str, float], has_headers=False)

    return dict(prices)

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
