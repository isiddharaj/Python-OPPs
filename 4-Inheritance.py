#Demonstrate multilevel inheritance using Person → Employee → Manager

class Person:
    def education(self):
        print("Graduation Education")

class Employee(Person):
    def company(self):
        print("Infosys")

class Manager(Employee):
    def department(self):
        print("Admin department")

m=Manager()
m.department()
m.company()
m.education()