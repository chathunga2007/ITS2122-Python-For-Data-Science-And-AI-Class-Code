cart = [12.99, 45.50, 8.25, 150.00, 22.10, 99.99] 

cart[2] = 9.50
print(cart)

cart.append(35.00)
print(cart)
cart.remove(150.00)
print(cart)

total = 0
for i in cart:
    total+=i
print(total)

for i in cart:
    if i > 50.00:
        i = i * 0.90
print(cart)

budget_item = []

for i in cart:
    if i < 25.00:
        budget_item.append(i)
print(budget_item)