from order import Order
from supplier import Supplier
from physical_product import PhysicalProduct
from discount_strategy import (
    NoDiscount,
    BulkDiscount,
    PercentageDiscount,
    StudentDiscount
)

# Create a sample supplier and product
supplier = Supplier(
    "S001",
    "Test Supplier",
    "test@example.com"
)

product = PhysicalProduct(
    "P001",
    "Desk Lamp",
    250.00,
    10,
    1.0,
    supplier
)

# Create an order with BulkDiscount
order = Order("ORD001", BulkDiscount(200, 20))
order.add_order_line(product, 1)

# Test BulkDiscount
assert order.calculate_total() == 230.00
print("BulkDiscount test passed!")

# Change strategy to PercentageDiscount
order.set_discount(PercentageDiscount(10))

assert order.calculate_total() == 225.00
print("PercentageDiscount and set_discount test passed!")

# Change strategy to StudentDiscount
order.set_discount(StudentDiscount())

assert order.calculate_total() == 237.50
print("StudentDiscount test passed!")

# Change strategy to NoDiscount
order.set_discount(NoDiscount())

assert order.calculate_total() == 250.00
print("NoDiscount test passed!")

# Test default strategy
default_order = Order("ORD002")
default_order.add_order_line(product, 1)

assert default_order.calculate_total() == 250.00
print("Default NoDiscount test passed!")

print("\nAll Order strategy tests passed!")