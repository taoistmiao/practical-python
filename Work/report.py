# report.py
#
# Exercise 2.4
import csv

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
            holding = {}
            holding["name"] = row[0]
            holding["shares"] = int(row[1])
            holding["price"] = float(row[2])
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

# Computes the gain or loss
cost = 0
value = 0
portfolio = read_portfolio("Data/portfolio.csv")
prices = read_prices("Data/prices.csv")
for stock in portfolio:
    cost += stock["shares"] * stock["price"]
    value += stock["shares"] * prices[stock["name"]]
if cost > value:
    print(f"The loss is {cost-value}")
else:
    print(f"The gain is {value-cost}")
