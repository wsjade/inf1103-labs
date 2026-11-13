from product import Product


class OrderLine:
    def __init__(self, product: Product, quantity: int) -> None:
        self.__product: Product = product
        self.__quantity: int = quantity

    def calculate_subtotal(self) -> float:
        return self.__product.get_price() * self.__quantity

    def display_information(self) -> None:
        print(
            f"Product: {self.__product.get_name()} | "
            f"Quantity: {self.__quantity} | "
            f"Subtotal: ${self.calculate_subtotal():.2f}"
        )