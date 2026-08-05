#Create a Person class using a constructor to initialize name and age.

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("Name is: ",self.name)
        print("Age is: ",self.age)

p1=Person("ABC",21)
p2=Person("Pqr",23)
p3=Person("LMN",22)

p1.display()
p2.display()
p3.display()