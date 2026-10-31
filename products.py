class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        # 1. Type validation: ensure quantity is an integer (and not a boolean, since bool inherits from int)
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise TypeError(
                f"Expected quantity to be an int, got {type(quantity).__name__}"
            )

        # 2. Value validation: ensure quantity is non-negative
        if quantity < 0:
            raise ValueError(f"Quantity cannot be negative, got {quantity}")
        
        self.quantity = quantity
        if self.quantity == 0:
            self.actve = False

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.actve = True

    def deactivate(self):
        self.actve = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise TypeError(
                f"Expected quantity to be an int, got {type(quantity).__name__}"
            )
        if quantity < 1:
            raise ValueError(f"Quantity cannot be smaller then 1")

        self.quantity = self.quantity - quantity
        return self.price

if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=101)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()