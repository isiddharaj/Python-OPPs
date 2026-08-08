#Create a Product class and calculate discounted price.

class Product:
    def __init__(self,price,sellingprice):
        self.price=price
        self.sellingprice=sellingprice

    def display(self):
        print("Original price: ",self.price)
        print("Selling price: ",self.sellingprice)
        print("Discounted price:",self.price-self.sellingprice)

p=Product(50,20)
p.display()