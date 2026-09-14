student_name = "Chathunga Bimsara"
registration_no = "ICT2025"
course_name = "BSc Computer Science"
number_of_subjects = 5
total_marks = 420
maximum_marks = 500

# Calculate average marks
average_marks = total_marks / number_of_subjects

# Calculate percentage
percentage = (total_marks / maximum_marks) * 100

# Display Student Report
print("Student Report")
print("-" * 30)

print(f"Name           : {student_name}")
print(f"Registration No: {registration_no}")
print(f"Course         : {course_name}")
print(f"Subjects       : {number_of_subjects}")
print(f"Total Marks    : {total_marks}")
print(f"Percentage     : {percentage:.2f}%")
print(f"Average Marks  : {average_marks:.2f}")