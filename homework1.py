#დავალება N1

import json

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"

    def to_dict(self):
        return {"name": self.name, "price": self.price, "quantity": self.quantity}

    @staticmethod
    def from_dict(data):
        return Product(data['name'], data['price'], data['quantity'])

def serialize_products_to_file(products, filename):
    with open(filename, 'w') as file:
        json.dump([product.to_dict() for product in products], file)

def deserialize_products_from_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return [Product.from_dict(item) for item in data]

products = [
    Product("Laptop", 1200.99, 5),
    Product("Smartphone", 899.99, 10),
    Product("Tablet", 299.99, 8)
]

filename = "products.json"

serialize_products_to_file(products, filename)
print("Product information has been written to the file.")

loaded_products = deserialize_products_from_file(filename)
print("Product information has been read from the file.")

for product in loaded_products:
    print(product)
