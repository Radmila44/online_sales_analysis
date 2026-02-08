from product import Product
from product_manager import ProductManager

print("\nFinal Project - Rad sa GitHubom i Pythonom\n")

# Kreirana instanca ProductManager i dodjeljena promjenjivoj manager
manager = ProductManager()

# # Dodavanje proizvoda
p1 = Product("Mobilni", 1200.00, 5)
p2 = Product("Slušalice", 150.00, 10)
p3 = Product("Monitor", 500, 20)
p4 = Product("Tastatura", 200.00, 20)
p5 = Product("Miš", 30.00, 150)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)
manager.add_product(p4)
manager.add_product(p5)
