Inventory = {
    "Microchips": [50, 12.50],
    "Resistors": [500, 0.10],
    "Capacitors": [200, 0.45]
}

total_store_value = 0

for item, data in Inventory.items():
    quantity = data[0]
    price = data[1]
    total_store_value += quantity * price

print("Total Store Value:", total_store_value)