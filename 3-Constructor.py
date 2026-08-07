#Create a Mobile class that initializes brand,mode and price.

class Mobile:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

    def display(self):
        print("Mobile brand: ",self.brand)
        print("Mobile model: ",self.model)
        print("Mobile price: ",self.price)

m1=Mobile("Samsung","S25",70000)
m2=Mobile("Apple","17pro",120000)
print("Mobile 1")
m1.display()
print("\nMobile 2")
m2.display()
