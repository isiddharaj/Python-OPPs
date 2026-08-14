#Demonstrate single inheritance.(Create Vehicle class and inherit Car.)

class Vehicle:
    def speed(self):
        print("Vehicle can Accelerate")

class Car(Vehicle):
    def control(self):
        print("Car has Steering")

c=Car()
c.speed()
c.control()
