#Create a Rectangle class with length and width.Calculate the area.

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        print("Area of Rectangle:",self.length*self.width)

r=Rectangle(10,20)
r.area()