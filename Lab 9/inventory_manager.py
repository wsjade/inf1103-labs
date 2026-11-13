import json
import os
import csv
from supplier import Supplier
from inventory import Inventory
from product_factory import ProductFactory

inventory: Inventory = Inventory()


def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))

            if value <= 0:
                raise ValueError("Number must be greater than zero.")
                continue
            return value

        except ValueError:
            print("Please enter a valid positive number, e.g. 12.50.")


def load_inventory() -> None:
    global inventory
    inventory = Inventory()

    if os.path.exists("inventory.json"):
        print("inventory.json found.")

        try:
            with open("inventory.json", "r") as file:
                data = json.load(file)

            for item in data:
                supplier_data = item.get("supplier", {
                    "supplier_id": "S001",
                    "name": "Legacy Supplier",
                    "contact_email": "not-provided@example.com"
                })

                supplier = Supplier(
                    supplier_data["supplier_id"],
                    supplier_data["name"],
                    supplier_data["contact_email"]
                )

                product = ProductFactory.create(
                    product_type=item["type"],
                    product_id=item["id"],
                    name=item["name"],
                    price=item["price"],
                    stock_quantity=item["stock"],
                    supplier=supplier,
                    weight=item.get("weight"),
                    download_size=item.get("download_size")
                )


                inventory.add_product(product)

            print("Inventory loaded successfully.")

        except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
            print(f"Unable to load inventory: {error}")

    else:
        print("inventory.json not found. Starting with empty inventory.")


def save_inventory() -> None:
    data = [
        product.to_dict()
        for product in inventory.get_products()
    ]

    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Inventory saved successfully to inventory.json.")


def add_product() -> None:
    print("\nAdd New Product")
    print("1. Physical Product")
    print("2. Digital Product")

    product_type = input("Choose product type: ")

    if product_type not in ["1", "2"]:
        print("Invalid product type.")
        return

    product_id = input("Product ID: ")

    if inventory.find_product(product_id) is not None:
        print("Product ID already exists.")
        return

    product_name = input("Product Name: ")
    print("\nSupplier Details")
    supplier_id = input("Supplier ID: ")
    supplier_name = input("Supplier Name: ")
    supplier_email = input("Supplier Contact Email: ")

    supplier = Supplier(
        supplier_id,
        supplier_name,
        supplier_email
    )

    try:
        price = get_positive_float("Price: ")
        stock = int(input("Stock Quantity: "))

        if price < 0 or stock < 0:
            print("Price and stock cannot be negative.")
            return

        weight = None
        download_size = None

        if product_type == "1":
            weight = float(input("Weight (kg): "))

            if weight < 0:
                print("Weight cannot be negative.")
                return

            selected_type = "physical"
            
        else:
            download_size = float(input("Download Size (MB): "))

            if download_size < 0:
                print("Download size cannot be negative.")
                return

            selected_type = "digital"

        product = ProductFactory.create(
        product_type=selected_type,
        product_id=product_id,
        name=product_name,
        price=price,
        stock_quantity=stock,
        supplier=supplier,
        weight=weight,
        download_size=download_size
    )

    except ValueError:
        print("Please enter valid numeric values.")
        return

    inventory.add_product(product)

    print("Product added successfully!")


def update_stock() -> None:
    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ")

    product = inventory.find_product(product_id)

    if product is None:
        print("Product not found.")
        return

    print("Product Found:")
    print(f"Name: {product.get_name()}")
    print(f"Current Stock: {product.get_stock()}")

    try:
        new_stock = int(input("New Stock Quantity: "))

        if new_stock < 0:
            print("Stock cannot be negative.")
            return

    except ValueError:
        print("Please enter a valid stock quantity.")
        return

    product.update_stock(new_stock)

    print("Stock updated successfully!")


def search_product() -> None:
    print("\nSearch Product")

    product_id = input("Enter Product ID: ")

    product = inventory.find_product(product_id)

    if product is None:
        print("Product not found.")
    else:
        print("Product Found")
        print("-" * 48)
        product.display_information()
        product.display_supplier_information()
        print("-" * 48)


def main() -> None:
    load_inventory()

    while True:
        print("\n========================================")
        print("INVENTORY MANAGEMENT SYSTEM")
        print("========================================")
        print("----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("----------------------------")

        option = input("Enter option: ")

        if option == "1":
            inventory.display_all()

        elif option == "2":
            add_product()

        elif option == "3":
            update_stock()

        elif option == "4":
            search_product()

        elif option == "5":
            print("Saving inventory...")
            save_inventory()

        elif option == "6":
            print("Saving inventory before exit...")
            save_inventory()
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break

        else:
            print("Invalid option. Please try again.")


def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    loaded = 0

    try:
        file = open(path, newline="")

    except FileNotFoundError:
        print(f"Products file not found: {path}")

    else:
        with file:
            reader = csv.reader(file)

            # Skip the header row
            next(reader, None)

            for row in reader:
                try:
                    product_type, product_id, name, price, stock_quantity = row

                    product = ProductFactory.create(
                        product_type=product_type,
                        product_id=product_id,
                        name=name,
                        price=float(price),
                        stock_quantity=int(stock_quantity),
                        supplier=supplier,
                        weight=0.0,
                        download_size=0.0
                    )

                    inventory.add_product(product)
                    loaded += 1

                except ValueError as error:
                    print(f"Skipping invalid row {row}: {error}")

        print(f"{loaded} products loaded.")

    finally:
        print("Load attempt finished.")


if __name__ == "__main__":
    main()