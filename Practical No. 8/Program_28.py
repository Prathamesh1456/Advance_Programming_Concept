#28.	Implement functions to add/remove products, calculate subtotal, apply coupon discounts, calculate GST, and generate the final invoice.
def add_product(cart, product_name, price, quantity):
    if product_name in cart:
        cart[product_name]['quantity'] += quantity
    else:
        cart[product_name] = {'price': price, 'quantity': quantity}
    print(f"Added {quantity} of '{product_name}' to the cart.")
def remove_product(cart, product_name):
    if product_name in cart:
        del cart[product_name]
        print(f"Removed '{product_name}' from the cart.")
    else:
        print(f"Product '{product_name}' not found in the cart.")
def calculate_subtotal(cart):
    subtotal = sum(item['price'] * item['quantity'] for item in cart.values())
    return subtotal
def apply_coupon_discount(subtotal, discount_percentage):
    discount_amount = subtotal * (discount_percentage / 100)
    return discount_amount
def calculate_gst(subtotal, gst_percentage):
    gst_amount = subtotal * (gst_percentage / 100)
    return gst_amount
def generate_invoice(cart, discount_percentage, gst_percentage):
    subtotal = calculate_subtotal(cart)
    discount_amount = apply_coupon_discount(subtotal, discount_percentage)
    gst_amount = calculate_gst(subtotal - discount_amount, gst_percentage)
    final_total = subtotal - discount_amount + gst_amount

    print("\n--- Invoice ---")
    for product_name, details in cart.items():
        print(f"{product_name}: {details['quantity']} x {details['price']} = {details['quantity'] * details['price']}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Discount ({discount_percentage}%): -{discount_amount:.2f}")
    print(f"GST ({gst_percentage}%): +{gst_amount:.2f}")
    print(f"Final Total: {final_total:.2f}")
def main():
    cart = {}
    while True:
        print("\nShopping Cart Menu:")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Generate Invoice")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            product_name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter quantity: "))
            add_product(cart, product_name, price, quantity)
        elif choice == '2':
            product_name = input("Enter product name to remove: ")
            remove_product(cart, product_name)
        elif choice == '3':
            discount_percentage = float(input("Enter coupon discount percentage: "))
            gst_percentage = float(input("Enter GST percentage: "))
            generate_invoice(cart, discount_percentage, gst_percentage)
        elif choice == '4':
            print("Exiting the shopping cart system.")
            break
        else:
            print("Invalid choice. Please try again.")