# Student database stored as a list of dictionaries
students = [
    {
        "name": "Prathamesh",
        "roll_no": 101,
        "cgpa": 9.2,
        "hostel_status": "Hosteller",
        "address": "Room 304, Hostel Block A"
    },
    {
        "name": "Suresh",
        "roll_no": 102,
        "cgpa": 7.8,
        "hostel_status": "Hosteller",
        "address": "Room 305, Hostel Block A"
    },
    {
        "name": "Ramesh",
        "roll_no": 103,
        "cgpa": 8.5,
        "hostel_status": "Non-Hosteller",
        "address": "Kolhapur"
    }
]

search_roll = 102
for student in students:
    if student["roll_no"] == search_roll:
        print("--- Student Details Found ---")
        print(f"Name:          {student['name']}")
        print(f"Roll No:       {student['roll_no']}")
        print(f"CGPA:          {student['cgpa']}")
        print(f"Hostel Status: {student['hostel_status']}")
        print(f"Address:       {student['address']}")
        print("-----------------------------")
        student_found = True
        break 
if not student_found:
    print(f"Error: Student with Roll No {search_roll} not found.")


search_cgpa = 8.5
for student in students:
    if student["cgpa"] == search_cgpa:
        print("--- Student Details Found ---")
        print(f"Name:          {student['name']}")
        print(f"Roll No:       {student['roll_no']}")
        print(f"CGPA:          {student['cgpa']}")
        print(f"Hostel Status: {student['hostel_status']}")
        print(f"Address:       {student['address']}")
        print("-----------------------------")
        student_found = True
        break 
if not student_found:
    print(f"Error: Student with Roll No {search_cgpa} not found.")