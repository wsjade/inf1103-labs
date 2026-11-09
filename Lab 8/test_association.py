from supplier import Supplier
from physical_product import PhysicalProduct


# Create a supplier
supplier = Supplier(
    "S001",
    "Sunshine Electronics",
    "sunshine@gmail.com"
)

# Create a product and pass the supplier object
product = PhysicalProduct(
    "P001",
    "Wireless Mouse",
    25.9,
    50,
    0.2,
    supplier
)

print("Before deleting supplier variable:")
product.display_information()
product.display_supplier_information()

# Delete the supplier variable
del supplier

print("\nAfter deleting supplier variable:")
product.display_supplier_information()