from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory

supplier = Supplier("S001", "Sunshine Electronics", "sunshine@gmail.com")

mouse = PhysicalProduct (
"P001", "Wireless Mouse", 25.9, 50, 0.2, supplier
)

software = DigitalProduct (
"P002", "Keyboard Software", 49.9, 20, 500, supplier
)

inventory = Inventory()
inventory.add_product(mouse)
inventory.add_product(software)

print("=== Testing Polymorphism ===")

for product in inventory.get_products():
    product.display_information()
    print(product.get_fulfilment_info())
    print()