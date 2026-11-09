
from product import Product
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory


# A function that accepts any Product
def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


supplier = Supplier("S001", "Sunshine Electronics", "sunshine@gmail.com")

# Create both product types
physical = PhysicalProduct(
    "P001", "Wireless Mouse", 25.9, 50, 0.2, supplier
)

digital = DigitalProduct(
    "P002", "Keyboard Software", 49.9, 20, 500, supplier
)


# Test 1: Both products can use the same function
print("=== Testing Substitutability ===")

show_product_details(physical)
print()

show_product_details(digital)


# Test 2: Both products can be added to Inventory
print("\n=== Testing Inventory ===")

inventory = Inventory()

inventory.add_product(physical)
inventory.add_product(digital)

inventory.display_all()

# Test normal inventory operations
print("\n=== Searching for Products ===")

found_product = inventory.find_product("P001")

if found_product is not None:
    found_product.display_information()

print("\n=== Updating Stock ===")

physical.update_stock(40)
digital.update_stock(15)

inventory.display_all()