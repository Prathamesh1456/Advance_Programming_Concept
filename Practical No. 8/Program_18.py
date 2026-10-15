#18.	Create a function that accepts marks in five subjects and returns the student's percentage and grade.
def calculate_percentage_and_grade(marks):
    total_marks = sum(marks)
    percentage = (total_marks / 500) * 100

    if percentage >= 90:
        grade = 'A'
    elif percentage >= 80:
        grade = 'B'
    elif percentage >= 70:
        grade = 'C'
    elif percentage >= 60:
        grade = 'D'
    else:
        grade = 'F'

    return percentage, grade
sub1 = float(input("Enter marks for subject 1: "))
sub2 = float(input("Enter marks for subject 2: "))
sub3 = float(input("Enter marks for subject 3: "))
sub4 = float(input("Enter marks for subject 4: "))
sub5 = float(input("Enter marks for subject 5: "))
marks = [sub1, sub2, sub3, sub4, sub5]
percentage, grade = calculate_percentage_and_grade(marks)
print(f"The student's percentage is: {percentage:.2f}%")