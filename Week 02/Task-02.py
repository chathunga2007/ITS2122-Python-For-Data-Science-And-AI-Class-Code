marks = [75, 82, 68, 91, 84]

marks.insert(3, 88)

total = sum(marks)

percentage_of_total = (total / (len(marks) * 100)) * 100

print(percentage_of_total)