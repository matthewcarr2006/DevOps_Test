# 3. Create a Car class with attributes make, model, and year. 
# Add methods to get and set the values of the attributes. 


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_make(self):
        return self.make
    
    def set_make(self, make):
        self.make = make

    def get_model(self):
        return self.model
    
    def set_model(self, model):
        self.model = model
    
    def get_year(self):
        return self.year
    
    def set_year(self, year):
        self.year = year

    def __str__(self):
        return F"{self.make} {self.model} {self.year}"
    

car = Car("Ford", "Focus", 2020)

print(car.get_make())
car.set_make("Toyota")
car.set_model("Pickup")
car.set_year(1995)
print(car.get_make())
print(car.get_model())
print(car.get_year())
print(car)
