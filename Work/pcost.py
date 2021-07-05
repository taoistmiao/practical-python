# pcost.py
#
# Exercise 1.27
# import csv
from os import read
import sys
from report import read_portfolio

def portfolio_cost(filename):
    cost = 0
    portfolio = read_portfolio(filename)
    for record in portfolio:
        cost += record["shares"] * record["price"]

    return cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)
print("Total cost", round(cost, 2))

