import math

marks = [72, 85, 91, 68, 85, 77, 93, 56, 72, 88, 95, 64, 79, 91, 83]

print("Original Marks:", marks)

marks_asc = sorted(marks)
print("Ascending Order:", marks_asc)

marks_desc = sorted(marks, reverse=True)
print("Descending Order:", marks_desc)

unique_marks_set = set(marks)
print("Unique Marks:", unique_marks_set)

unique_marks_list = sorted(list(unique_marks_set))
print("Unique Sorted List:", unique_marks_list)

total_marks = sum(marks)
print("Total Marks:", total_marks)

num_stu = len(marks)
average = total_marks / num_stu
print("Average: ", average)

highest_mark = max(marks)
print("Highest Mark:", highest_mark)

lowest_mark = min(marks)
print("Lowest Mark:", lowest_mark)

marks_range = highest_mark - lowest_mark
print("Range:", marks_range)

sum_squared_diff = sum((x - average) ** 2 for x in marks)
variance = sum_squared_diff / num_stu
print("Variance:", variance)

standard_deviation = math.sqrt(variance)
print("Standard Deviation (SD):", standard_deviation)