import random

# List of menu items as dictionaries
menu_items = [
    {'item_code': 'D1', 'description': 'SODA', 'price': 3, 'stock': None},  # Drink (no stock limit)
    {'item_code': 'D2', 'description': 'LEMONADE', 'price': 3, 'stock': None},
    {'item_code': 'D3', 'description': 'TEA', 'price': 2, 'stock': None},
    {'item_code': 'D4', 'description': 'WATER', 'price': 0, 'stock': None},
    {'item_code': 'A1', 'description': 'POTATO_CAKES', 'price': 7, 'stock': random.randint(25, 50)},
    {'item_code': 'A2', 'description': 'SPINACH_DIP', 'price': 5, 'stock': random.randint(25, 50)},
    {'item_code': 'A3', 'description': 'OYSTERS', 'price': 13, 'stock': random.randint(25, 50)},
    {'item_code': 'A4', 'description': 'CHEESE_FRIES', 'price': 4, 'stock': random.randint(25, 50)},
    {'item_code': 'A5', 'description': 'ONION_RINGS', 'price': 7, 'stock': random.randint(25, 50)},
    {'item_code': 'S1', 'description': 'COBB', 'price': 14, 'stock': random.randint(25, 50)},
    {'item_code': 'S2', 'description': 'CAESAR', 'price': 13, 'stock': random.randint(25, 50)},
    {'item_code': 'S3', 'description': 'GREEK', 'price': 12, 'stock': random.randint(25, 50)},
    {'item_code': 'E1', 'description': 'BURGER', 'price': 16, 'stock': random.randint(25, 50)},
    {'item_code': 'E2', 'description': 'PASTA', 'price': 15, 'stock': random.randint(25, 50)},
    {'item_code': 'E3', 'description': 'GNOCCHI', 'price': 14, 'stock': random.randint(25, 50)},
    {'item_code': 'E4', 'description': 'GRILLED_STEAK_SANDWICH', 'price': 17, 'stock': random.randint(25, 50)},
    {'item_code': 'T1', 'description': 'CARAMEL_CHEESECAKE', 'price': 13, 'stock': random.randint(25, 50)},
    {'item_code': 'T2', 'description': 'APPLE_COBBLER', 'price': 12, 'stock': random.randint(25, 50)},
    {'item_code': 'T3', 'description': 'BROWNIE_SUNDAE', 'price': 9, 'stock': random.randint(25, 50)},
    {'item_code': 'T4', 'description': 'FLAN', 'price': 8, 'stock': random.randint(25, 50)},
]

# Function to display menu
def display_menu():
    for item in menu_items:
        stock_info = f" (Stock: {item['stock']})" if item['stock'] is not None else ""
        print(f"{item['item_code']} - {item['description']} - ${item['price']}{stock_info}")

