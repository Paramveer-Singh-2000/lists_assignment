import random

# Initial menu with stock numbers assigned for non-drink items
menu_items = [
    {"code": "D1", "description": "SODA", "price": 3, "stock": None},
    {"code": "D2", "description": "LEMONADE", "price": 3, "stock": None},
    {"code": "D3", "description": "TEA", "price": 2, "stock": None},
    {"code": "D4", "description": "WATER", "price": 0, "stock": None},
    {"code": "A1", "description": "POTATO_CAKES", "price": 7, "stock": random.randint(25, 50)},
    {"code": "A2", "description": "SPINACH_DIP", "price": 5, "stock": random.randint(25, 50)},
    {"code": "A3", "description": "OYSTERS", "price": 13, "stock": random.randint(25, 50)},
    {"code": "A4", "description": "CHEESE_FRIES", "price": 4, "stock": random.randint(25, 50)},
    {"code": "A5", "description": "ONION_RINGS", "price": 7, "stock": random.randint(25, 50)},
    {"code": "S1", "description": "COBB", "price": 14, "stock": random.randint(25, 50)},
    {"code": "S2", "description": "CAESAR", "price": 13, "stock": random.randint(25, 50)},
    {"code": "S3", "description": "GREEK", "price": 12, "stock": random.randint(25, 50)},
    {"code": "E1", "description": "BURGER", "price": 16, "stock": random.randint(25, 50)},
    {"code": "E2", "description": "PASTA", "price": 15, "stock": random.randint(25, 50)},
    {"code": "E3", "description": "GNOCCHI", "price": 14, "stock": random.randint(25, 50)},
    {"code": "E4", "description": "GRILLED_STEAK_SANDWICH", "price": 17, "stock": random.randint(25, 50)},
    {"code": "T1", "description": "CARAMEL_CHEESECAKE", "price": 13, "stock": random.randint(25, 50)},
    {"code": "T2", "description": "APPLE_COBBLER", "price": 12, "stock": random.randint(25, 50)},
    {"code": "T3", "description": "BROWNIE_SUNDAE", "price": 9, "stock": random.randint(25, 50)},
    {"code": "T4", "description": "FLAN", "price": 8, "stock": random.randint(25, 50)},
]

# Function to display the menu
def display_menu():
    for item in menu_items:
        stock_info = f"(Stock: {item['stock']})" if item['stock'] is not None else ""
        print(f"{item['code']} - {item['description']} - ${item['price']} {stock_info}")
