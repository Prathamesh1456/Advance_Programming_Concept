#21.	Create a function that accepts item prices and quantities and returns the total bill after applying a discount.
def calculate_total_bill(prices, quantities, discount_percentage):
    total_amount = sum(price * quantity for price, quantity in zip(prices, quantities))
    discount_amount = (discount_percentage / 100) * total_amount
    total_bill = total_amount - discount_amount
    return total_bill
prices = [100, 200, 150]
quantities = [2, 1, 3]
discount_percentage = float(input("Enter discount percentage: "))
total_bill = calculate_total_bill(prices, quantities, discount_percentage)
print(f"The total bill after applying a discount of {discount_percentage}% is: {total_bill}")
