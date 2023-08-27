'''
Input:
You are provided with a database containing a Product class
with attributes (id, name, cost, description, image path).
Your goal is to create an array of product instances.

Objectives:

Create a ProductViewModel class that will be used
for displaying products on a web app's client interface.
The ProductViewModel should only present products
with specific attributes: id, name, and cost.
Implement a function to sort the array of product
objects, excluding those with empty cost or description values.
'''


class Product():
    def __init__(self, id: int, name: str, cost: float, description: str, image_path: str):
        self.id = id
        self.name = name
        self.cost = cost
        self.description = description
        self.image_path = image_path


class ProductViewModel(Product):
    def __init__(self, id: int, name: str, cost: float):
        super().__init__(id, name, cost, "", "~/img")


def show_products(data):
    filtered_products = []

    for product in data:
        # Execute products with empty cost or description values:
        if product.cost is not None and product.description:
            product_view_model = ProductViewModel(product.id, product.name, product.cost)
            filtered_products.append(product_view_model)

    # Sort the list of ProductViewModel objects based on cost
    sorted_products = sorted(filtered_products, key=lambda product: product.cost)   # here you can change for product.id | cost | name ...
    for product in sorted_products:
        print(f"ID: {product.id}, Name: {product.name}, Cost: ${product.cost}")


if __name__ == '__main__':
    item_1 = Product(1, 'Book', 55.4, 'Book for programing', '')
    item_2 = Product(2, 'Trimmer', 32.1, '', '')
    item_3 = Product(3, 'Printer', 120.0, 'Printer for print', '')
    item_4 = Product(4, 'Steamer', 0, 'Steamer for cloth', '')
    item_5 = Product(5, 'Ink', 21.2, 'Inks for printer', '')

    data = [item_1, item_2, item_3, item_4, item_5]

    print(show_products(data))
