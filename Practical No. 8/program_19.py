# 19.	Write a function that accepts the number of units consumed and calculates the electricity bill according to predefined slabs.
def calculate_electricity_bill():
    num_of_units = int(input("Enter the number of units consumed: "))
    if num_of_units <= 100:
        bill_amount = num_of_units * 5
    elif num_of_units <= 200:
        bill_amount = (100 * 5) + ((num_of_units - 100) * 7)
    elif num_of_units <= 300:
        bill_amount = (100 * 5) + (100 * 7) + ((num_of_units - 200) * 10)
    else:
        bill_amount = (100 * 5) + (100 * 7) + (100 * 10) + ((num_of_units - 300) * 15)
    return bill_amount
consumption = calculate_electricity_bill()
print(f"The electricity bill for {consumption} units is: {consumption} currency units")