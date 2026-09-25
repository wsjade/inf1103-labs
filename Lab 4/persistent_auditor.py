def get_valid_input():
    stock = input("Enter stock quantity or 'quit': ")

    if stock == "quit":
        return "quit"

    try:
        stock = int(stock)
    except ValueError:
        print("Error: Please enter a valid number.")
        return None

    if stock < 0:
        print("Error: Stock quantity cannot be negative.")
        return None

    return stock

def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total
    
def calculate_tax(amount):
    tax = amount * 0.10
    return tax


def generate_report(total_units, total_deliveries, failed_attempts):
    print("Total Units Processed:", total_units)
    print("Total Deliveries Processed:", total_deliveries)
    print("Number of Failed/Rejected Entries:", failed_attempts)

def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            inventory = int(file.readline().strip())
            return inventory
    except FileNotFoundError:
        return 0

def save_inventory(inventory, transaction_history):
    with open("inventory.txt", "w") as file:
        file.write(str(inventory) + "\n")
        file.write(str(transaction_history) + "\n")


inventory = load_inventory()
failed_entries = 0
deliveries = 0
transaction_history = []


while True:
    stock = get_valid_input()

    if stock == "quit":
        save_inventory(inventory, transaction_history)
        break

    if stock is None:
        failed_entries = failed_entries + 1
        continue

    inventory = process_delivery(inventory, stock)
    deliveries = deliveries + 1
    transaction_history.append(stock)

    tax = calculate_tax(stock)

    if inventory > 500:
        print("ALERT: Overstock limit exceeded! Please keep it at 500.")
        break

generate_report(inventory, deliveries, failed_entries)
print("Transaction History:", transaction_history)