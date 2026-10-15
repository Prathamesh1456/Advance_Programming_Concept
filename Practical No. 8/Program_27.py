#27.	Create functions to calculate consultation charges, laboratory charges, medicine charges, room charges, and final bill. Apply discounts based on patient category.

def calculate_consultation_charges(patient_category):
    if patient_category == 'general':
        return 100
    elif patient_category == 'senior':
        return 80
    elif patient_category == 'student':
        return 50
    else:
        return 0
def calculate_laboratory_charges(tests_conducted):
    test_costs = {
        'blood_test': 200,
        'x_ray': 500,
        'mri': 1500,
        'ct_scan': 1200
    }
    total_lab_charges = sum(test_costs.get(test, 0) for test in tests_conducted)
    return total_lab_charges
def calculate_medicine_charges(medicines):
    medicine_costs = {
        'paracetamol': 10,
        'antibiotic': 50,
        'painkiller': 20,
        'vitamins': 30
    }
    total_medicine_charges = sum(medicine_costs.get(med, 0) for med in medicines)
    return total_medicine_charges
def calculate_room_charges(room_type, days_stayed):
    room_costs = {
        'general': 500,
        'semi_private': 1000,
        'private': 2000
    }
    return room_costs.get(room_type, 0) * days_stayed
def calculate_final_bill(patient_category, tests_conducted, medicines, room_type, days_stayed):
    consultation_charges = calculate_consultation_charges(patient_category)
    laboratory_charges = calculate_laboratory_charges(tests_conducted)
    medicine_charges = calculate_medicine_charges(medicines)
    room_charges = calculate_room_charges(room_type, days_stayed)

    total_bill = consultation_charges + laboratory_charges + medicine_charges + room_charges

    if patient_category == 'senior':
        discount = 0.1 * total_bill  
    elif patient_category == 'student':
        discount = 0.15 * total_bill  
    else:
        discount = 0

    final_bill = total_bill - discount
    return final_bill, discount
def main():
    patient_category = input("Enter patient category (general/senior/student): ").lower()
    tests_conducted = input("Enter tests conducted (comma-separated, e.g., blood_test,x_ray): ").split(',')
    medicines = input("Enter medicines prescribed (comma-separated, e.g., paracetamol,antibiotic): ").split(',')
    room_type = input("Enter room type (general/semi_private/private): ").lower()
    days_stayed = int(input("Enter number of days stayed: "))

    final_bill, discount = calculate_final_bill(patient_category, tests_conducted, medicines, room_type, days_stayed)

    print(f"\nFinal Bill: {final_bill:.2f} currency units")
    print(f"Discount Applied: {discount:.2f} currency units")
