#23.	Write a program using separate functions to process student records containing name, roll number, and marks in five subjects. Calculate total, percentage, grade, class average, highest scorer, and lowest scorer.
def calculate_total(marks):
    return sum(marks)
def calculate_percentage(total, num_subjects):
    return (total / (num_subjects * 100)) * 100
def determine_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'
def process_student_records(students):
    total_marks = []
    for student in students:
        name, roll_number, marks = student
        total = calculate_total(marks)
        percentage = calculate_percentage(total, len(marks))
        grade = determine_grade(percentage)
        total_marks.append(total)
        print(f"Name: {name}, Roll Number: {roll_number}, Total: {total}, Percentage: {percentage:.2f}%, Grade: {grade}")
    
    class_average = sum(total_marks) / len(total_marks)
    highest_scorer = students[total_marks.index(max(total_marks))]
    lowest_scorer = students[total_marks.index(min(total_marks))]
    
    print(f"\nClass Average: {class_average:.2f}")
    print(f"Highest Scorer: {highest_scorer[0]} with Total Marks: {max(total_marks)}")
    print(f"Lowest Scorer: {lowest_scorer[0]} with Total Marks: {min(total_marks)}")

# Example student records
#Taing input for student records
num_students = int(input("Enter the number of students: "))
students = []
for _ in range(num_students):
    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    marks = []
    for i in range(5):
        mark = float(input(f"Enter marks for subject {i + 1}: "))
        marks.append(mark)
    students.append((name, roll_number, marks))

process_student_records(students)
