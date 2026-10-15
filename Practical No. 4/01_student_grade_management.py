# 1.	Write a program to building a simple student grade management system for a class of students. The system will store student names and their grades (both as lists) and should be able to perform the following operations:
# ●	Add a new student and their grade.
# ●	Update the grade of an existing student.
# ●	Remove a student from the list.
# ●	Calculate and display the average grade of the class.
# ●	Display the highest and lowest grades in the class.
# ●	Use lists to store the student names and their corresponding grades.
# ●	Implement functions to add, update, remove, and calculate the average and extreme grades.

students = []
grades = []

def add_student():
    name = input("Enter student name: ")
    grade = float(input("Enter student grade: "))
    students.append(name)
    grades.append(grade)

def update_grade():
    name = input("Enter student name: ")
    if name in students:
        index = students.index(name)
        new_grade = float(input("Enter new grade: "))
        grades[index] = new_grade
    else:
        print("Student not found.")

def remove_student():
    name = input("Enter student name: ")
    if name in students:
        index = students.index(name)
        students.pop(index)
        grades.pop(index)
    else:
        print("Student not found.")

def calculate_average():
    if grades:
        average = sum(grades) / len(grades)
        print(f"Average grade: {average}")
    else:
        print("No grades available.")

def display_highest_lowest():
    if grades:
        print(f"Highest grade: {max(grades)}")
        print(f"Lowest grade: {min(grades)}")
    else:
        print("No grades available.")

#Using a simple menu to perform operations
while True:
    print("\nStudent Grade Management System")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Remove Student")
    print("4. Calculate Average Grade")
    print("5. Display Highest and Lowest Grades")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        update_grade()
    elif choice == '3':
        remove_student()
    elif choice == '4':
        calculate_average()
    elif choice == '5':
        display_highest_lowest()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")

