
class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # Private attribute

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative")
        else:
            self._price = value

    @price.deleter
    def price(self):
        print(f"Deleting price for {self.name}")
        del self._price

product= Product("Laptop", 1000)
print(product.price)

product.price = 1100
print(product.price)

product.price =  -100

del product.price

