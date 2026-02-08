class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

# Metod za prikaz informacija o proizvodu
    def display_info(self):
        print(f"Proizvod: {self.name:15} | Cijena: {self.price:>8.2f} KM | Količina: {self.quantity:>5}")

# Metod za ažuriranje količine proizvoda
    def update_quantity(self, new_quantity):
        if new_quantity >= 0:
            self.quantity = new_quantity
        else:
            print(f"Greška: Količina za {self.name} ne može biti negativna!")