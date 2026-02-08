from product import Product
from product_manager import ProductManager

print("\nFinal Project - Rad sa GitHubom i Pythonom\n")

# Kreirana instanca ProductManager i dodjeljena promjenjivoj manager
manager = ProductManager()

# # Dodavanje proizvoda
p1 = Product("Laptop", 1200.00, 5)
p2 = Product("Slušalice", 150.00, 10)
p3 = Product("Monitor", 500, 10)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

# Prikaz svih proizvoda
manager.display_all_products()

# Ukupna vrijednost inventara
manager.total_value()
