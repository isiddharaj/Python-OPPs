#Create a Movie class and print movie details using constructor values.

class Movie:
    def __init__(self,name,screen,seat,price,time):
        self.name=name
        self.screen=screen
        self.seat=seat
        self.price=price
        self.time=time

    def  display(self):
        print("Movie Name: ",self.name)
        print("Movie Screen: ",self.screen)
        print("Movie Seat:",self.seat)
        print("Ticket Price:",self.price)
        print("Movie Time:",self.time)

m1=Movie("Spider-Man","A1(3D)",24,399,"10:00am")
m2=Movie("Oddesy","A3(IMAX)",18,511,"1:00pm")
m3=Movie("Dhamaal Again","A2",8,299,"3:00pm")

print("Today's Show")
print("\nMovie 1:---")
m1.display()
print("\nMovie 2:---")
m2.display()
print("\nMovie 3:---")
m3.display()