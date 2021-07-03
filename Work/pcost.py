# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):

    cost = 0
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        header = next(rows) # skip header
        for line, row in enumerate(rows, start=1):
            try:
                shares = int(row[1])
                price = float(row[2])
                cost += shares * price
            except ValueError:
                print(f"Line {line}: Couldn't convert: {row}")
    return cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)
print("Total cost", round(cost, 2))

