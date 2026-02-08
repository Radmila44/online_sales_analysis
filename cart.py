from product_manager import ProductManager
from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []

# Metod za dodavanje proizvoda u korpu        
    def add_cart(self, product):
        if product.quantity > 0:
            self.cart_items.append(product)
            product.quantity -= 1
            print(f"Dodano u korpu: {product.name}.")
        else:
            print(f"Nema dovoljno {product.name} na stanju!")
 
# Metod za racunanje ukupne vrijednosti korpe            
    def total_cart(self):
        return sum(product.price for product in self.cart_items)

# metod za prikazivanje sadržaja korpe  
    def display_cart(self):
        print("\n-----VAŠA KORPA------")
        for product in self.cart_items:
            print(f"- {product.name:10}: {product.price:8.2f} KM")
        print(f"\nZA PLATITI: {self.total_cart():10.2f} KM.")
        print("--------------------------\n")