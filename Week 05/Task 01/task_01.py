weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

def calculate_bmi(weight, height):
    bmi = weight / (height * height)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi > 18.5 or bmi < 24.9:
        category = "Normal"
    elif bmi > 25 or bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi, category

bmi_value, status = calculate_bmi(weight, height)
print(bmi_value)
print(status)
