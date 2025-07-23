import products
import store


# Setup initial inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
]
best_buy = store.Store(product_list)


def run_store_interface(store_instance):
    """Run interactive command-line interface for store operations."""
    while True:
        print("\n--- Store Menu ---")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Choose an option (1–4): ")
        print("-----")

        if choice in ("1", "3"):
            for index, product in enumerate(store_instance.get_all_products()):
                print(f"{index + 1}. {product.show()}")

        if choice == "2":
            print(f"Total of {store_instance.get_total_quantity()} items in store")

        if choice == "3":
            print("-----")
            print("When you want to finish order, enter empty text.")
            product_num = input("Which product # do you want? ")

            if product_num == "":
                continue

            product_amount = input("Which amount do you want? ")

            if product_amount == "":
                continue

            try:
                product_index = int(product_num) - 1
                quantity = int(product_amount)

                if 0 <= product_index < len(product_list):
                    selected_product = product_list[product_index]
                    total = selected_product.buy(quantity)

                    if selected_product.has_errors():
                        print("⚠️ Error(s):")
                        for err in selected_product.get_errors():
                            print(f"- {err}")
                    else:
                        print(f"Product added to order! Total: €{total:.2f}")
                else:
                    print("Invalid product number.")

            except (ValueError, IndexError):
                print("Invalid input. Please enter numeric values.")

        if choice == "4":
            print("👋 Goodbye!")
            break


def main():
    """Launch CLI interface for store operations."""
    run_store_interface(best_buy)


if __name__ == '__main__':
    main()
