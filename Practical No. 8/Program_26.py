#26.	Develop a modular program using functions to calculate electricity bills using different consumption slabs. Include fixed charges, taxes, and discounts.
def calculate_electricity_bill(units_consumed):
    slabs = [
        (100, 5),   
        (200, 7),  
        (300, 10), 
        (float('inf'), 15) 
    ]
    
    fixed_charge = 50 
    tax_rate = 0.1 
    discount_rate = 0.05  

    bill_amount = fixed_charge
    remaining_units = units_consumed

    for slab_limit, rate in slabs:
        if remaining_units <= 0:
            break
        if remaining_units > slab_limit:
            bill_amount += slab_limit * rate
            remaining_units -= slab_limit
        else:
            bill_amount += remaining_units * rate
            remaining_units = 0

    tax_amount = bill_amount * tax_rate
    discount_amount = bill_amount * discount_rate

    total_bill = bill_amount + tax_amount - discount_amount

    return total_bill, tax_amount, discount_amount
def main():
    units_consumed = int(input("Enter the number of units consumed: "))
    total_bill, tax_amount, discount_amount = calculate_electricity_bill(units_consumed)

    print(f"Total Bill Amount: {total_bill:.2f} currency units")
    print(f"Tax Amount: {tax_amount:.2f} currency units")
    print(f"Discount Amount: {discount_amount:.2f} currency units")
    