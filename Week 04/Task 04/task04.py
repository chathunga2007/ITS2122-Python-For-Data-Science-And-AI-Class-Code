num = int(input("Enter your number: "))
fact = 1

if num < 0:
    print("Invalid Number!")
else:
    for i in range(1, num+1):
        fact*=i
print(fact)