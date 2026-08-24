sales = [12000, 15000, 18000, 16000, 20000]

sales.insert(3, 22000)
sales.sort()

minimum = sales[0]
maximum = sales[-1]

increase = ((maximum - minimum) / minimum) * 100

print("Sales:", sales)
print("Percentage Increase:", increase)