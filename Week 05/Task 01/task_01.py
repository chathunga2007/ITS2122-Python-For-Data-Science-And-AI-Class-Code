weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

def calculate_bmi(weight, height):
    BMI = weight / (height * height)

    return BMI

result = calculate_bmi(weight, height)
print(result)

if result < 18.5:
    print("Underweight")
elif result > 18.5 or result < 24.9:
    print("Normal")
elif result > 25 or result < 29.9:
    print("Overweight")
else:
    print("Obese")