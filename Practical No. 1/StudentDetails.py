def addStudent():
    rollNo = int(input("Enter Roll: "))
    name = input("Enter Name: ")
    cgpa = float(input("Enter your CGPA: "))
    hostel = input("Is Hostel Available (Y/N): ").strip().upper()
    HostelStatus = True if hostel == "Y" else False
    address = input("Enter Address: ")
    student = {
        "RollNo": rollNo,
        "Name": name,
        "CGPA": cgpa,
        "HostelStatus": HostelStatus,
        "Address": address,
    }
    return student
students = []
while True:
    students.append(addStudent())

    choice = input("Do you want to add another student? (Y/N): ").strip().upper()
    if choice != "Y":
        break
search_name = input("Enter the name of the student you want to search for: ")
found = False
for student in students:
    if student["Name"].strip().lower() == search_name.strip().lower():
        print(f"\nDetails for {student['Name']}:")
        print(f"Roll No: {student['RollNo']}")
        print(f"CGPA: {student['CGPA']}")
        print(f"Hostel Status: {'Yes' if student['HostelStatus'] else 'No'}")
        print(f"Address: {student['Address']}")
        found = True
        break 
if not found:
    print(f"Student named '{search_name}' not found.")