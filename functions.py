# Import menu_items from data.py
from data import menu_items

# Manager function to update item price or description
def update_menu_item(code, new_description=None, new_price=None):
    for item in menu_items:
        if item['code'] == code:
            if new_description:
                item['description'] = new_description
            if new_price:
                item['price'] = new_price
            print(f"Item {code} updated: {item}")
            return
    print(f"Item {code} not found in menu.")

# Function to add a new item to the menu
def add_menu_item(code, description, price, stock=None):
    if any(item['code'] == code for item in menu_items):
        print(f"Item with code {code} already exists.")
    else:
        new_item = {"code": code, "description": description, "price": price, "stock": stock}
        menu_items.append(new_item)
        print(f"Item {code} added to the menu.")

# Function to remove an item from the menu
def remove_menu_item(code):
    for i, item in enumerate(menu_items):
        if item['code'] == code:
            del menu_items[i]
            print(f"Item {code} removed from the menu.")
            return
    print(f"Item {code} not found in menu.")

# Function to display the updated menu
def display_updated_menu():
    for item in menu_items:
        stock_info = f"(Stock: {item['stock']})" if item['stock'] is not None else ""
        print(f"{item['code']} - {item['description']} - ${item['price']} {stock_info}")
