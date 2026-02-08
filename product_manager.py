from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

# Metod za dodavanje proizvoda
    def add_product(self, product):
        self.products.append(product)
        print(f"Proizvod '{product.name}' je uspješno dodan.")

# Metod za prikaz svih proizvoda
    def display_all_products(self):
        print("\n--- DOSTUPNI PROIZVODI ---")
        for product in self.products:
            product.display_info()
        print("-------------------------")

# Metod za prikaz ukupne vrijednosti svih proizvoda
    def total_value(self):
        total = sum(product.price * product.quantity for product in self.products)
        print(f"\nUKUPNA VRIJEDNOST SVIH PROIZVODA: {total:.2f} KM\n")
        return total