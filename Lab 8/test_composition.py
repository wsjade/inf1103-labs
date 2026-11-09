from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from order import Order


# Create a supplier
supplier = Supplier("S001", "Sunshine Electronics", "sunshine@gmail.com")

# Create products
mouse = PhysicalProduct("P001", "Wireless Mouse", 25.9, 50, 0.2, supplier)
software = DigitalProduct("P002", "Keyboard Software", 49.9, 20, 500, supplier)

# Create an order
order = Order("ORD001")

# Add products to the order
order.add_order_line(mouse, 2)
order.add_order_line(software, 1)

# Display order total
print("Order ID:", order.order_id)
print(f"Order Total: ${order.calculate_total():.2f}")

# Check that the original products still exist
print("\nProducts still exist independently:")
print(mouse.get_name())
print(software.get_name())