from product import Product
from product_manager import ProductManager
from cart import Cart

print("\nFinal Project - Rad sa GitHubom i Pythonom\n")

# Kreirana instanca ProductManager i dodjeljena promjenjivoj manager
manager = ProductManager()

# # Dodavanje proizvoda
p1 = Product("Laptop", 1200.00, 5)
p2 = Product("Slušalice", 150.00, 10)
p3 = Product("Monitor", 500.00, 10)
p4 = Product("Tastatura", 200.00, 20)
p5 = Product("Miš", 30.00, 100)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)
manager.add_product(p4)
manager.add_product(p5)

# Prikaz svih proizvoda
manager.display_all_products()

# Ukupna vrijednost inventara
manager.total_value()

# Kreirana instanca Cart i dodjeljena promjenjivoj my_cart
my_cart = Cart()

my_cart.add_cart(p1)
my_cart.add_cart(p3)
my_cart.add_cart(p4)

my_cart.total_cart()
my_cart.display_cart()

manager.display_all_products()
