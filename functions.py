from data import menu_items

def take_order(item_code, quantity=None, orders=None):
    """
    Take customer order and check stock availability. For drinks, no stock check.
    """
    for item in menu_items:
        if item['item_code'].upper() == item_code.upper():
            if item['stock'] is None:  # No stock limit for drinks
                print(f"Order confirmed: {quantity if quantity else 1}x {item['description']} (No stock limit).")
                orders.append({'description': item['description'], 'price': item['price'], 'quantity': quantity if quantity else 1})
            elif item['stock'] >= (quantity or 1):
                item['stock'] -= (quantity or 1)
                print(f"Order confirmed: {quantity if quantity else 1}x {item['description']}.")
                print(f"Remaining stock for {item['description']}: {item['stock']}")
                orders.append({'description': item['description'], 'price': item['price'], 'quantity': quantity if quantity else 1})
            else:
                print(f"Sorry, only {item['stock']} {item['description']} available.")
            return
    print("Item not found.")
