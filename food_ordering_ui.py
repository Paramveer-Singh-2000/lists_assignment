import functions

def show_main_menu():
    while True:
        print("Paramveer's Diner")
        print("__________________")
        print('N for a new order')
        print('C to change order')
        print('X for close orders and print the check')
        print('Q for quit')
        user_menu_choice = input('Your choice: ')
        
        if user_menu_choice in 'Qq':
            break
        elif user_menu_choice in 'Xx':
            close_order()
        elif user_menu_choice in 'Nn':
            print('Starting new order...')
            make_order()
        elif user_menu_choice in 'Cc':
            change_order()

def make_order():
    while True:
        print("Menu:")
        functions.show_menu()
        
        # Get item code input
        item_code = input('Enter item code (or Q to quit): ').upper()
        if item_code in 'Qq':
            break
        elif item_code not in functions.menu:
            print(f"Invalid item code: {item_code}. Please try again.")
            continue
        
        # Get quantity input
        try:
            quantity = int(input(f'Enter quantity for {item_code}: '))
            if quantity <= 0:
                print("Quantity should be greater than 0.")
                continue
            functions.add_item_to_order(item_code, quantity)
        except ValueError:
            print("Invalid quantity. Please enter a valid number.")

def close_order():
    print('Your final order:')
    functions.print_check()

def change_order():
    print('Modifying existing order:')
    functions.show_order()
    item_code = input("Enter item code to modify: ").upper()
    try:
        new_quantity = int(input("Enter new quantity (or 0 to remove item): "))
        functions.modify_order(item_code, new_quantity)
    except ValueError:
        print("Invalid quantity. Please enter a valid number.")

if __name__ == '__main__':
    show_main_menu()