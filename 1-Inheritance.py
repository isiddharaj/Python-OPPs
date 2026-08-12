#Create a Person class and inherit it into a Student class

class Person:
    def learn(self):
        print("Person can learn")

class Student(Person):
    def fast(self):
        print("Student can learn fast")

s=Student()
s.learn()
s.fast()