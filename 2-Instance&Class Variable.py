#Create a class with a class variable shared among all objects.
#----IMP----
class Animal:
    noise="Makes Noise"

    def __init__(self,name):
        self.name = name

    def display(self):
        print("Animal Name: ",self.name)
        print(Animal.noise)

a1=Animal("Dog")
a2=Animal("Cat")

a1.display()
print()
a2.display()