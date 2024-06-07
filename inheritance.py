class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year
    
    def display_info(self):
        super().display_info()
        print(f"Year: {self.year}")

class Motorcycle(Vehicle):
    def __init__(self, make, model, color):
        super().__init__(make, model)
        self.color = color
    
    def display_info(self):
        super().display_info()
        print(f"Color: {self.color}")

# Test cases
car = Car("Toyota", "Camry", 2020)
car.display_info()  

motorcycle = Motorcycle("Honda", "CBR500R", "Red")
motorcycle.display_info()
