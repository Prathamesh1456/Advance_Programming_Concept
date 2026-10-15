# Classroom Attendance System

attendance = {}

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for day in days:
    students = set(input("Enter students present on " + day + ": ").split())
    attendance[day] = students

# Students who attended all classes
all_students = set.intersection(*attendance.values())

# Count attendance of each student
student_count = {}

for students in attendance.values():
    for student in students:
        student_count[student] = student_count.get(student, 0) + 1

# Students who attended only one class
one_class = {student for student in student_count if student_count[student] == 1}

# Total unique students
unique_students = set.union(*attendance.values())

print("\nAttendance:")
print(attendance)

print("\nStudents who attended all classes:", all_students)
print("Students who attended only one class:", one_class)
print("Total unique students:", len(unique_students))