#4]Create a Student class where college name is common for all students
#Change a class variable and observe the effect on all objects.

class Student():
    college="IIT Madras"

    def __init__(self,name):
        self.name=name

    def display(self):
        print("Enter Student Name: ",self.name)
        print("College is",Student.college)

s1=Student("ABC")
s2=Student("XYZ")
s3=Student("PQR")

s1.display()
print()
s2.display()
print()
s3.display()