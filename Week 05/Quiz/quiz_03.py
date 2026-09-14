password = "Py@th0n2023!" 

if len(password) >= 8:
    print("Valid Length")
else:
    print("Too Short")

digit_count = 0

for i in password:
    if i.isdigit():
        digit_count+=1
print(digit_count)

has_special = False

for i in password:
    if i == "@" or i == "#" or i == "!":
        has_special = True
        break
print(has_special)

first_three = password[:3]
last_four = password[-4:]

print(first_three)
print(last_four)

attempts = 3

while attempts > 0:
    attempts -= 1
    print("Attempt failed.", attempts, "attempts remaining.")