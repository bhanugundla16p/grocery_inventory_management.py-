# Grocery store inventory management using Python

# Initialize an empty inventory list
inventory = []

def add_item(name, quantity, price):
    # Check if the item already exists in the inventory
    for item in inventory:
        if item['name'] == name:
            item['quantity'] += quantity
            print(f"Updated quantity of {name} to {item['quantity']}.")
            return

    # If the item doesn't exist, add it to the inventory
    inventory.append({'name': name, 'quantity': quantity, 'price': price})
    print(f"Added {quantity} {name}(s) to the inventory.")

def update_item_quantity(name, new_quantity):
    # Update the quantity of an existing item
    for item in inventory:
        if item['name'] == name:
            item['quantity'] = new_quantity
            print(f"Updated quantity of {name} to {new_quantity}.")
            return

    # If the item doesn't exist, print a message
    print(f"{name} not found in the inventory.")

def display_inventory():
    # Display the current inventory
    if not inventory:
        print("Inventory is empty.")
    else:
        print("Current Inventory:")
        for item in inventory:
            print(f"{item['name']}: {item['quantity']} - Price: ${item['price']} per item")

# Main program loop
while True:
    print("\nMenu:")
    print("1. Add new item")
    print("2. Update item quantity")
    print("3. View inventory")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        name = input("Enter the name of the item: ")
        quantity = int(input("Enter the quantity to add: "))
        price = float(input("Enter the price per item: $"))
        add_item(name, quantity, price)
    elif choice == '2':
        name = input("Enter the name of the item: ")
        new_quantity = int(input("Enter the new quantity: "))
        update_item_quantity(name, new_quantity)
    elif choice == '3':
        display_inventory()
    elif choice == '4':
        print("Exiting the inventory management system.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

# End of the program
