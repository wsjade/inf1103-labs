from product_factory import ProductFactory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier

supplier = Supplier(
    "S001",
    "Test Supplier",
    "test@example.com"
)

# Test physical product creation
physical = ProductFactory.create(
    "physical", "P001", "Desk Lamp",
    25.00, 10, supplier, weight=1.5
)

assert isinstance(physical, PhysicalProduct)
print("Physical product factory test passed!")

# Test digital product creation
digital = ProductFactory.create(
    "digital", "D001", "Photo Editor",
    49.90, 100, supplier, download_size=500.0
)

assert isinstance(digital, DigitalProduct)
print("Digital product factory test passed!")

# Test unknown product type
try:
    ProductFactory.create(
        "service", "S001", "Installation",
        30.00, 5, supplier
    )
    assert False, "Expected ValueError was not raised."

except ValueError as error:
    assert str(error) == "Unknown product type: service"
    print("Unknown product type test passed!")

print("\nAll Factory tests passed!")