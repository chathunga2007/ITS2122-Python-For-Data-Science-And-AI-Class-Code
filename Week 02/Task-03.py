temperatures = [32, 27, 35, 21, 29, 37, 30]

temperatures.insert(2, 34)
temperatures.sort()

temperature_range = max(temperatures) - min(temperatures)

print(temperature_range)