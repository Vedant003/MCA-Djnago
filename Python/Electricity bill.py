units = float(input("Enter the number of units consumed: "))

if units <= 50:
    cost = units * 0.50
elif units <= 150:
    cost = 50 + (units - 50) * 0.75
elif units <= 250:
    cost = 50 + 100 + (units - 150) * 1.20
else:
    cost = 50 + 100 + 100 + (units - 250) * 1.50

total_cost = cost + cost * 0.20  # Adding 20% surcharge
print(f"The electricity bill is: {total_cost}")
