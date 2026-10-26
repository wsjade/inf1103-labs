import json
import os

from product import Product
from inventory import Inventory

inventory = Inventory()


def load_inventory():
    global inventory
    inventory = Inventory()

    if os.path.exists("inventory.json"):
        print("inventory.json found.")

        try:
            with open("inventory.json", "r") as file:
                data = json.load(file)

            for item in data:
                product = Product(
                    item["id"],
                    item["name"],
                    item["price"],
                    item["stock"]
                )
                inventory.add_product(product)

            print("Inventory loaded successfully.")

        except (json.JSONDecodeError, KeyError, TypeError) as error:
            print(f"Unable to load inventory: {error}")

    else:
        print("inventory.json not found. Starting with empty inventory.")


def save_inventory():
    data = [
        product.to_dict()
        for product in inventory.get_products()
    ]

    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Inventory saved successfully to inventory.json.")


def add_product():
    print("\nAdd New Product")

    product_id = input("Product ID: ")

    if inventory.search_product(product_id) is not None:
        print("Product ID already exists.")
        return

    product_name = input("Product Name: ")

    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))

        if price < 0 or stock < 0:
            print("Price and stock cannot be negative.")
            return

    except ValueError:
        print("Please enter a valid price and stock quantity.")
        return

    product = Product(product_id, product_name, price, stock)
    inventory.add_product(product)

    print("Product added successfully!")

