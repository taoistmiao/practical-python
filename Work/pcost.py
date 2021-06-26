# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):

    cost = 0
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        header = next(rows) # remove header in processing
        for row in rows:
            try:
                shares = int(row[1])
                price = float(row[2])
                cost += shares * price
            except ValueError:
                print("Invalid literal in line:", ",".join(row))
    return cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)
print("Total cost", round(cost, 2))

