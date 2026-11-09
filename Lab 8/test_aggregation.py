from supplier import Supplier
from physical_product import PhysicalProduct
from inventory import Inventory


# Create a supplier
supplier = Supplier(
    "S001",
    "Sunshine Electronics",
    "sunshine@gmail.com"
)

# Create a product independently
product = PhysicalProduct(
    "P001",
    "Wireless Mouse",
    25.9,
    50,
    0.2,
    supplier
)

# Create two inventories
inventory_a = Inventory()
inventory_b = Inventory()

# Add product to Inventory A
inventory_a.add_product(product)

print("Product in Inventory A:")
inventory_a.display_all()

# Remove product from Inventory A
inventory_a.remove_product("P001")

print("\nAfter removing product from Inventory A:")
inventory_a.display_all()

# Check that the product still exists
print("\nDoes the product still exist?")
print(product.get_name())

# Add the same product to Inventory B
inventory_b.add_product(product)

print("\nProduct in Inventory B:")
inventory_b.display_all()