import functions
from data import display_menu

# Global variable to store orders
orders = []

# Main function to show the menu
def show_main_menu():
    while True:
        print("Paramveer's Dinner")
        print("__________________")
        print("N for a new order")
        print("C to change order")
        print("R to reset the order")
        print("X for close orders and print the check")
        print("Q for quit")
        user_menu_choice = input("Your choice: ").strip().upper()

        if user_menu_choice == 'Q':
            break
        elif user_menu_choice == 'X':
            print("Closing the order...")
            print_check()
        elif user_menu_choice == 'N':
            print("Starting new order...")
            make_order()
        elif user_menu_choice == 'C':
            print("Changing the order...")
            # Logic to modify the order can be added here
        elif user_menu_choice == 'R':
            print("Resetting the order list.")
            reset_order()

# Function to make an order
def make_order():
    print("Menu:")
    display_menu()
    while True:
        user_input = input("Enter item code and quantity (or Q to quit): ").strip().upper()
        if user_input == 'Q':
            break

        try:
            item_code, quantity = user_input.split()
            quantity = int(quantity)
        except ValueError:
            item_code = user_input
            quantity = None  # Default to None for drinks (no stock limit)

        functions.take_order(item_code, quantity, orders)

# Function to print the check
def print_check():
    total = 0
    print("\nYour Order Summary:")
    print("Item\t\tQuantity\tPrice\tSubtotal")
    for item in orders:
        price = item['price']
        quantity = item['quantity']
        subtotal = price * quantity
        total += subtotal
        print(f"{item['description']}\t{quantity}\t\t${price}\t${subtotal}")

    tax_rate = 0.1  # 10% tax
    tax = total * tax_rate
    grand_total = total + tax

    print(f"\nTotal: ${total:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Grand Total: ${grand_total:.2f}\n")

# Function to reset the order
def reset_order():
    global orders
    orders = []
    print("Order has been reset.")

if __name__ == "__main__":
    show_main_menu()
