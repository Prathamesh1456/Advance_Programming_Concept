# Inventory Management System

inventory = {}


def add_product():
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    inventory[name] = quantity
    print("Product added successfully.")


def update_product():
    name = input("Enter product name to update: ")

    if name in inventory:
        quantity = int(input("Enter new quantity: "))
        inventory[name] = quantity
        print("Quantity updated successfully.")
    else:
        print("Product not found.")


def highest_stock():
    if inventory:
        product = max(inventory, key=inventory.get)
        print("Product with highest stock:", product)
        print("Quantity:", inventory[product])
    else:
        print("Inventory is empty.")


def remove_product():
    name = input("Enter product name to remove: ")

    if name in inventory and inventory[name] == 0:
        del inventory[name]
        print("Product removed successfully.")
    else:
        print("Product is not sold out or not found.")


def display_inventory():
    print("\nInventory:", inventory)
    print("Total unique products:", len(inventory))


# Menu
while True:
    print("\n--- Inventory Management System ---")
    print("1. Add Product")
    print("2. Update Product")
    print("3. Find Highest Stock")
    print("4. Remove Sold Out Product")
    print("5. Display Inventory")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        update_product()
    elif choice == "3":
        highest_stock()
    elif choice == "4":
        remove_product()
    elif choice == "5":
        display_inventory()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")