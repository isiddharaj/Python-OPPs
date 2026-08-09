#Create a class with one instance variable and display it
class Animal:
    def __init__ (self,name):
        self.name=name

    def display(self):
        print("Enter Animal Name: ",self.name)


a=Animal("Dog")
a.display()