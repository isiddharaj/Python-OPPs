#Create a Car class with brand and model. Create two objects and print their details.

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def display(self):
        print("Brand:",self.brand)
        print("Model:",self.model)

car1=Car("Toyota","Fortuner")
car2=Car("BMW","M4")

car1.display()
car2.display()


