
students = []
grades = []

def add_student():
    name = input("Enter student name: ")
    grade = float(input("Enter student grade: "))
    students.append(name)
    grades.append(grade)
    print("Student added successfully.\n")

def update_grade():
    name = input("Enter student name to update: ")
    if name in students:
        index = students.index(name)
        new_grade = float(input("Enter new grade: "))
        grades[index] = new_grade
        print("Grade updated successfully.\n")
    else:
        print("Student not found.\n")


def remove_student():
    name = input("Enter student name to remove: ")
    if name in students:
        index = students.index(name)
        students.pop(index)
        grades.pop(index)
        print("Student removed successfully.\n")
    else:
        print("Student not found.\n")

def average_grade():
    if len(grades) > 0:
        avg = sum(grades) / len(grades)
        print("Average Grade:", avg)
    else:
        print("No students in the list.")
    print()


def highest_lowest():
    if len(grades) > 0:
        print("Highest Grade:", max(grades))
        print("Lowest Grade:", min(grades))
    else:
        print("No students in the list.")
    print()


def display_students():
    if len(students) > 0:
        print("\nStudent List:")
        for i in range(len(students)):
            print(students[i], "-", grades[i])
    else:
        print("No students available.")
    print()


while True:
    print("===== Student Grade Management System =====")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Remove Student")
    print("4. Calculate Average Grade")
    print("5. Display Highest and Lowest Grades")
    print("6. Display All Students")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        update_grade()
    elif choice == "3":
        remove_student()
    elif choice == "4":
        average_grade()
    elif choice == "5":
        highest_lowest()
    elif choice == "6":
        display_students()
    elif choice == "7":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.\n")



        # 11  14   17  18   19   20   23   