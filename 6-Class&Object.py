#Create a Laptop class with brand, RAM, and processor. Display all specifications.

class Laptop:
    def __init__(self,brand,ram,processor):
        self.brand=brand
        self.ram=ram
        self.processor=processor

    def display(self):
        print("Brand is: ",self.brand)
        print("RAM is:",self.ram,"GB")
        print("Processor is: ",self.processor)

l1=Laptop("Dell",16,"AMD")
l2=Laptop("Lenovo",12,"Intel")
l3=Laptop("Acer",8,"Intel")

l1.display()
l2.display()
l3.display()