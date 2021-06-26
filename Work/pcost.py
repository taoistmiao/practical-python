# pcost.py
#
# Exercise 1.27

cost = 0
with open("Data/portfolio.csv", "rt") as f:
    header = next(f)
    for line in f:
        row = line.split(",")
        shares = int(row[1])
        price = float(row[2])
        cost += shares * price
print("Total cost", round(cost, 2))

