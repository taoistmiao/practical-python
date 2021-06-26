# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):

    cost = 0
    with open(filename, "rt") as f:
        header = next(f)
        for line in f:
            row = line.split(",")
            shares = int(row[1])
            price = float(row[2])
            cost += shares * price
    return cost

cost = portfolio_cost("Data/portfolio.csv")
print("Total cost", round(cost, 2))

