a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b:
    a, b = b, a

if a > c:
    a, c = c, a

if b > c:
    b, c = c, b

print("Ascending order:", a, b, c)