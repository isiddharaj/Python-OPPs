# #Create a Circle class that calculates the circumference using a method.
#
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#
#     def circumference(self):
#         print("Circumference of Circle is:",2*3.14*self.radius)
#
# c=Circle(5)
# c.circumference()
#

#----without constructor------
r=int(input("enter the radius:"))
class Circle:
    def circumference(self):
        c=2*3.14*r
        print("the circumference of the circle is ",c)

circle=Circle()
circle.circumference()