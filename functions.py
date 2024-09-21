import data  # Import menu data from data.py

order = []

# Parse the menu using data from data.py
def parse_menu():
    menu = {}
    for item in data.menu_items:
        parts = item.split()
        code = parts[0]
        description = '_'.join(parts[1:-1])  # Join all middle parts as the description
        price = parts[-1]  # The last part is the price
        menu[code] = {
            'description': description,
            'price': float(price)
        }
    return menu

menu = parse_menu()

# Show menu items grouped by category
def show_menu():
    def display_items(item_codes, category):
        print(f"\n{category}:")
        for item_code in item_codes:
            print(f"{item_code}: {menu[item_code]['description']} - ${menu[item_code]['price']}")

    display_items(data.drink_items, "Drinks")
    display_items(data.appetizer_items, "Appetizers")
    display_items(data.salad_items, "Salads")
    display_items(data.entree_items, "Entrees")
    display_items(data.dessert_items, "Desserts")

# Add an item to the order
def add_item_to_order(item_code, quantity):
    if item_code not in menu:
        print(f"Item {item_code} not found.")
        return
    item = menu[item_code]
    order.append((item_code, item, quantity))
    print(f"Added {quantity}x {item['description']} to your order.")

# Print the current order
def print_check():
    if not order:
        print("Your order is empty!")
        return

    print("\nCurrent Order:")
    subtotal = 0
    for item_code, item, quantity in order:
        item_total = item['price'] * quantity
        subtotal += item_total
        print(f"{quantity}x {item['description']} @ ${item['price']} each: ${item_total:.2f}")

    # Calculate totals
    tax = subtotal * 0.08  # Assuming 8% tax
    total = subtotal + tax

    print(f"\nSubtotal: ${subtotal:.2f}")
    print(f"Tax (8%): ${tax:.2f}")
    print(f"Total: ${total:.2f}")

# Modify the quantity of an item in the order
def modify_order(item_code, new_quantity):
    for i, (code, item, quantity) in enumerate(order):
        if code == item_code:
            if new_quantity == 0:
                del order[i]  # Remove item if quantity is set to 0
                print(f"Removed {item_code} from your order.")
            else:
                order[i] = (item_code, item, new_quantity)  # Update the quantity
                print(f"Updated {item_code} to {new_quantity}x.")
            return
    print(f"Item {item_code} not found in your order.")

# Reset the order list
def reset_order():
    global order
    order = []
    print("Your order has been reset.")

# Show current order summary without printing the check
def show_order():
    if not order:
        print("Your order is empty.")
    else:
        print("Current items in your order:")
        for item_code, item, quantity in order:
            print(f"{quantity}x {item['description']} @ ${item['price']} each")
