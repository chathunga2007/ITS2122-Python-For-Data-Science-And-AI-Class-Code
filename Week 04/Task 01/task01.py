input1 = float(input("Enter the length of the first side: "))
input2 = float(input("Enter the length of the second side: "))

if input1 > 0 and input2 > 0:
    hypotenuse = (input1**2 + input2**2)**0.5
    print("The length of the hypotenuse is:", hypotenuse)
else:
    print("Error: Triangle sides must be positive numbers")