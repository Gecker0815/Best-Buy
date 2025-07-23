# 🛍️ Store Inventory CLI

This project is a command-line inventory management tool for handling products in a store. It allows users to browse products, view total stock, and place orders interactively.

## 📦 Features

- View all active products
- Show total stock quantity in store
- Place orders by selecting product and quantity
- Validate user input and handle errors gracefully

## 🧩 Structure

- `Product`: Represents a single product with name, price, quantity, and activation state.
- `Store`: Manages a collection of products and handles ordering logic.
- `main.py`: Entry point with interactive menu (CLI interface).

## ✅ Error Handling

- Ensures invalid inputs (e.g. wrong types, too high quantities) are captured internally.
- Errors for each product are stored via `product.has_errors()` and `product.get_errors()`.

## 🚀 Getting Started

```bash
python main.py
```

You’ll be greeted by an interactive menu to view products, place orders, and exit the store.

## 💡 Notes

- The interface runs entirely in the terminal.
- Input validation prevents crashes, and meaningful feedback is provided.
- Ideal for teaching OOP, input handling, and basic inventory systems.
