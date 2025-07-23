class Store:
    """Manage product inventory."""

    def __init__(self, products=None):
        """Initialize the store."""
        if products is None:
            products = []
        self.products = products

    def add_product(self, product):
        """Add product to store."""
        self.products.append(product)

    def remove_product(self, product):
        """Remove product from store."""
        self.products.remove(product)

    def get_total_quantity(self):
        """Return total quantity of active products."""
        return sum(
            product.get_quantity()
            for product in self.products
            if product.is_active()
        )

    def get_all_products(self):
        """List all active products."""
        return [
            product
            for product in self.products
            if product.is_active()
        ]

    def order(self, shopping_list):
        """Process purchase and return total cost."""
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price
