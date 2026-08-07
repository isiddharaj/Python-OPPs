#Create a Student class with roll number and marks using a constructor

class Student:
    def __init__(self,rollno,marks):
        self.rollno=rollno
        self.marks=marks

    def display(self):
        print("Student Roll_Number: ",self.rollno)
        print("Student Marks: ",self.marks)

s1=Student(rollno=10,marks=80)
s2=Student(23,94)
s1.display()
s2.display()