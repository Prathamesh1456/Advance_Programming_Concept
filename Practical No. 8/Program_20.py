#20. Write a function that accepts basic salary and calculates gross salary after adding HRA and DA.

def calculate_gross_salary(basic_salary):
    hra = 0.2 * basic_salary
    da = 0.1 * basic_salary
    gross_salary = basic_salary + hra + da
    return gross_salary
basic_salary = float(input("Enter the basic salary: "))
gross_salary = calculate_gross_salary(basic_salary)
print(f"The gross salary is: {gross_salary}")