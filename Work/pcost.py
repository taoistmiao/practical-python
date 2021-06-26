# pcost.py
#
# Exercise 1.27
import csv

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

cost = portfolio_cost("Data/portfolio.csv")
print("Total cost", round(cost, 2))

