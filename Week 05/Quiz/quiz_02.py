grades = {
    "Alice": 85, 
    "Bob": 58, 
    "Charlie": 92, 
    "Diana": 45, 
    "Evan": 78
}

grades["Fiona"] = 88
print(grades)

for key, value in grades.items():
    print("Student", key, "achieved a score of", value)

pass_mark = 60
pass_count = 0

for i in grades.values():
    if i >= pass_mark:
        pass_count+=1
print(pass_count)

highest_score = 0
highest_student = ""

for name, score in grades.items():
    if score > highest_score:
        highest_score = score
        highest_student = name
print("Student Name: ", highest_student)
print("Highest Socre: ", highest_score)

for i in grades:
    grades[i] += 5
    if grades[i] > 100:
        grades[i] = 100
print(grades)