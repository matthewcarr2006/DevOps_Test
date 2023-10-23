# 4. Create a Product class with attributes name, price, and quantity. 
# Add methods to calculate the total value of the product (price * quantity) 
# and add or remove items from the product inventory. 

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity
    
    def add_items(self, quantity):
        self.quantity += quantity

    def remove_itmes(self, quantity):
        if quantity > self.quantity:
            print("Insufficient quantity")
        else:
            self.quantity -= quantity
    
    def __str__(self):
        return f"{self.name} {self.price} {self.quantity}"
    

prod = Product("macbook pro", 1000, 5)

print(prod.total_value)
prod.add_items(5)
print(prod.quantity)
prod.remove_itmes(9)
print(prod.quantity)
prod.remove_itmes(5)
print(prod)
