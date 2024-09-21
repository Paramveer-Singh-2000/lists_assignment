menu_items = [
    'D1 SODA 3', 'D2 LEMONADE 3', 'D3 TEA 2', 'D4 WATER 0',
    'A1 POTATO_CAKES 7', 'A2 SPINACH_DIP 5', 'A3 OYSTERS 13', 
    'A4 CHEESE_FRIES 4', 'A5 ONION_RINGS 7', 'S1 COBB 14',
    'S2 CAESAR 13', 'S3 GREEK 12', 'E1 BURGER 16', 'E2 PASTA 15',
    'E3 GNOCCHI 14', 'E4 GRILLED_STEAK_SANDWICH 17', 
    'T1 CARAMEL_CHEESECAKE 13', 'T2 APPLE_COBBLER 12', 
    'T3 BROWNIE_SUNDAE 9', 'T4 FLAN 8'
]

order = []

def parse_menu():
    menu = {}
    for item in menu_items:
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

def show_menu():
    print("\nDrinks:")
    for item_code in ['D1', 'D2', 'D3', 'D4']:
        print(f"{item_code}: {menu[item_code]['description']} - ${menu[item_code]['price']}")
    
    print("\nAppetizers:")
    for item_code in ['A1', 'A2', 'A3', 'A4', 'A5']:
        print(f"{item_code}: {menu[item_code]['description']} - ${menu[item_code]['price']}")
    
    print("\nSalads:")
    for item_code in ['S1', 'S2', 'S3']:
        print(f"{item_code}: {menu[item_code]['description']} - ${menu[item_code]['price']}")
    
    print("\nEntrees:")
    for item_code in ['E1', 'E2', 'E3', 'E4']:
        print(f"{item_code}: {menu[item_code]['description']} - ${menu[item_code]['price']}")
    
    print("\nDesserts:")
    for item_code in ['T1', 'T2', 'T3', 'T4']:
        print(f"{item_code}: {menu[item_code]['description']} - ${menu[item_code]['price']}")

def add_item_to_order(item_code, quantity):
    if item_code not in menu:
        print(f"Item {item_code} not found.")
        return
    item = menu[item_code]
    order.append((item_code, item, quantity))
    print(f"Added {quantity}x {item['description']} to your order.")
