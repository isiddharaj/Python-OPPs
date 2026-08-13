#Create an Animal class and derive a Dog class

class Animal:
    def walk(self):
        print("Animal can Walk")

class Dog(Animal):
    def dog_walk(self):
        print("Dog Walks on 4 legs")

d=Dog()
d.walk()
d.dog_walk()
