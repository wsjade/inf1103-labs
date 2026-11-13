from supplier import Supplier
from physical_product import PhysicalProduct
from order_line import OrderLine

supplier = Supplier(
    "S001",
    "Test Supplier",
    "test@example.com"
)

# Create a valid product for testing
product = PhysicalProduct(
    "P001",
    "Desk Lamp",
    25.00,
    10,
    1.5,
    supplier
)

# Test invalid product price
try:
    PhysicalProduct(
        "P002", "Invalid Product", 0,
        10, 1.0, supplier
    )
    assert False, "Expected ValueError for invalid price."

except ValueError as error:
    assert str(error) == "Price must be greater than zero."
    print("Invalid price test passed!")

# Test negative stock
try:
    PhysicalProduct(
        "P003", "Invalid Stock", 25.00,
        -5, 1.0, supplier
    )
    assert False, "Expected ValueError for negative stock."

except ValueError as error:
    assert str(error) == "Stock quantity cannot be negative."
    print("Negative stock test passed!")

# Test updating stock to a negative number
try:
    product.update_stock(-5)
    assert False, "Expected ValueError for negative stock update."

except ValueError as error:
    assert str(error) == "Stock quantity cannot be negative."
    print("Negative stock update test passed!")

# Test invalid order quantity
try:
    OrderLine(product, 0)
    assert False, "Expected ValueError for invalid quantity."

except ValueError as error:
    assert str(error) == "Quantity must be greater than zero."
    print("Invalid order quantity test passed!")

print("\nAll validation tests passed!")