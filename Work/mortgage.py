# mortgage.py
#
# Exercise 1.7
principal = 500_000.0
rate = 0.05
default_payment = 2684.11
total_paid = 0.0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

month = 0
while principal > 0:
    month += 1
    payment = default_payment + extra_payment if month >= extra_payment_start_month and month <= extra_payment_end_month  else default_payment
    principal = principal * (1+rate/12) - payment
    if (principal < 0):
        payment += principal
        principal = 0
    total_paid = total_paid + payment
    print(f"{month}\t {round(total_paid,2)}\t {round(principal, 2)}")

print(f"Total paid\t {round(total_paid, 2)}")
print(f"Month\t\t {month}")

