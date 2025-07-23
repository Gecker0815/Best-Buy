class Product:
    """Represents a store product."""

    def __init__(self, name, price, quantity):
        """Initialize product with name, price, and quantity."""
        self.name = name if isinstance(name, str) else "Unknown"
        self.price = price if isinstance(price, (int, float)) else 0.0
        self.quantity = quantity if isinstance(quantity, int) else 0
        self.active = True
        self._errors = []

        if not isinstance(name, str):
            self._errors.append("Invalid name type.")
        if not isinstance(price, (int, float)):
            self._errors.append("Invalid price type.")
        if not isinstance(quantity, int):
            self._errors.append("Invalid quantity type.")

    def get_quantity(self):
        """Return current quantity."""
        return self.quantity

    def set_quantity(self, quantity):
        """Update product quantity."""
        if isinstance(quantity, int) and quantity >= 0:
            self.quantity = quantity
        else:
            self._errors.append("Invalid quantity update.")

    def is_active(self):
        """Check if product is active."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self):
        """Return formatted product info."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        """Buy given quantity, update stock, and return total price."""
        if not isinstance(quantity, int) or quantity <= 0:
            self._errors.append("Invalid quantity to buy.")
            return 0.0

        if self.quantity - quantity < 0:
            self._errors.append("Not enough stock available.")
            return 0.0

        self.quantity -= quantity
        return float(quantity * self.price)

    def has_errors(self):
        """Check if the product encountered any errors."""
        return bool(self._errors)

    def get_errors(self):
        """Return list of recorded error messages."""
        return self._errors
