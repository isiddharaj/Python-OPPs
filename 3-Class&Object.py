#Create an Employee class with name and salary.Write a method to display employee information.

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def display(self):
        print("Name is:",self.name)
        print("Salary is:",self.salary)

e=Employee("Tony Stark",50000)
e.display()