class Product:
    def __init__(self, product_id, name, price, quantity, reorder_level):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.reorder_level = reorder_level


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self):
        product_id = input("Product ID: ")
        name = input("Product Name: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))
        reorder_level = int(input("Reorder Level: "))
        product = Product(product_id, name, price, quantity, reorder_level)
        self.products[product_id] = product
        print("Product added successfully!")

    def view_products(self):
        if not self.products:
            print("No products available.")
            return
        print("\nAvailable Products:")
        print("ID\tName\tPrice\tQty")
        for product in self.products.values():
            print(f"{product.product_id}\t{product.name}\t{product.price}\t{product.quantity}")

    def check_stock(self, product_id, qty):
        if product_id in self.products:
            return self.products[product_id].quantity >= qty
        return False

    def update_stock(self, product_id, qty):
        product = self.products[product_id]
        product.quantity -= qty
        if product.quantity <= product.reorder_level:
            print(f"⚠ Reorder Alert for product: {product.name}")


class Billing:
    def __init__(self):
        self.items = []

    def add_item(self, name, qty, price):
        self.items.append((name, qty, price))

    def generate_bill(self):
        print("\n------- BILL -------")
        total = 0
        for name, qty, price in self.items:
            amount = qty * price
            print(f"{name} x {qty} = ₹{amount}")
            total += amount
        print("--------------------")
        print(f"Total Amount: ₹{total}")
        print("--------------------")


class SupermarketApp:
    def __init__(self):
        self.inventory = Inventory()

    def menu(self):
        while True:
            print("\n--- Supermarket Menu ---")
            print("1. Add Product")
            print("2. View Products")
            print("3. Purchase Product")
            print("4. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                self.inventory.add_product()
            elif choice == "2":
                self.inventory.view_products()
            elif choice == "3":
                self.purchase_product()
            elif choice == "4":
                print("Thank you! Exiting...")
                break
            else:
                print("Invalid choice!")

    def purchase_product(self):
        bill = Billing()
        while True:
            product_id = input("Enter Product ID (or 'done'): ")
            if product_id.lower() == "done":
                break
            if product_id not in self.inventory.products:
                print("Product not found!")
                continue
            qty = int(input("Enter quantity: "))
            if self.inventory.check_stock(product_id, qty):
                product = self.inventory.products[product_id]
                bill.add_item(product.name, qty, product.price)
                self.inventory.update_stock(product_id, qty)
            else:
                print("Insufficient stock!")
        bill.generate_bill()


app = SupermarketApp()
app.menu()
