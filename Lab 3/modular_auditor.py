inventory = 0
failed_entries = 0

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


def get_valid_input():
    ...


def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total


def calculate_tax(amount):
    tax = amount * 0.10
    return tax

    print("Current inventory:", inventory)

    if inventory > 500:
        print("ALERT: Overstock limit exceeded! Please keep it at 500.")


print("Total Units Processed:", inventory)
print("Number of Failed/Rejected Entries:", failed_entries)