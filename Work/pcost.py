# pcost.py
#
# Exercise 1.27
# import csv
from report import read_portfolio

def portfolio_cost(filename):
    cost = 0
    portfolio = read_portfolio(filename)
    for record in portfolio:
        cost += record["shares"] * record["price"]

    return cost

def main(args):
    if len(args) == 2:
        filename = args[1]
    else:
        filename = "Data/portfolio.csv"

    cost = portfolio_cost(filename)
    print("Total cost", round(cost, 2))

if __name__ == "__main__":
    import sys
    main(sys.argv)
