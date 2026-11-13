import os
import tempfile
from unittest.mock import patch
from contextlib import redirect_stdout
from io import StringIO

from inventory import Inventory
from supplier import Supplier
from inventory_manager import get_positive_float, load_products


supplier = Supplier(
    "S001",
    "Test Supplier",
    "test@example.com"
)

# --------------------------------
# Test 1: Invalid user input
# --------------------------------
output = StringIO()

with patch("builtins.input", side_effect=["abc", "-5", "12.50"]):
    with redirect_stdout(output):
        result = get_positive_float("Enter price: ")

assert result == 12.50
assert "Please enter a valid positive number" in output.getvalue()

print("Invalid user input test passed!")


# --------------------------------
# Test 2: Missing CSV file
# --------------------------------
inventory = Inventory()
output = StringIO()

with redirect_stdout(output):
    load_products("missing_products.csv", inventory, supplier)

assert "Products file not found" in output.getvalue()
assert "Load attempt finished." in output.getvalue()

print("Missing CSV file test passed!")


# --------------------------------
# Test 3: Invalid CSV rows
# --------------------------------
csv_content = """product_type,product_id,name,price,stock_quantity
physical,P001,Desk Lamp,25.00,10
digital,D001,Photo Editor,49.90,100
service,S001,Installation,30.00,5
physical,P002,Office Chair,abc,3
physical,P003,Monitor Stand,39.50,7
"""

with tempfile.TemporaryDirectory() as temp_dir:
    csv_path = os.path.join(temp_dir, "products.csv")

    with open(csv_path, "w") as file:
        file.write(csv_content)

    inventory = Inventory()
    output = StringIO()

    with redirect_stdout(output):
        load_products(csv_path, inventory, supplier)

    result = output.getvalue()

    assert len(inventory.get_products()) == 3
    assert "3 products loaded." in result
    assert "Unknown product type: service" in result
    assert "could not convert string to float" in result

print("Invalid CSV rows test passed!")

print("\nAll exception handling tests passed!")