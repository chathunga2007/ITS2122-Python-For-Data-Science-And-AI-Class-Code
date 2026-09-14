def calculate_bill(customer, **items):
    # Calculate subtotal
    subtotal = sum(items.values())

    # Apply discount
    if subtotal >= 100:
        discount = subtotal * 0.20
    elif subtotal >= 50:
        discount = subtotal * 0.10
    else:
        discount = 0

    # Amount after discount
    discounted_amount = subtotal - discount

    # Add 5% service tax
    tax = discounted_amount * 0.05

    # Final total
    total = discounted_amount + tax

    # Return formatted bill
    return {
        "Customer": customer,
        "Subtotal": subtotal,
        "Discount": discount,
        "Tax": tax,
        "Total": total
    }
    

print(calculate_bill(customer="Kamal", burger=20, pizza=30, cola=5))