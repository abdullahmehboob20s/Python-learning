import os

os.system("cls")


class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The name of the Train is : {self.name}")
        print(f"The Seats available are : {self.seats}")

    def fareInfo(self):
        print(f"The Fare of the ticket is : Rs {self.fare}")

    def bookTicket(self):
        if (self.seats > 0):
            print(
                f"Your ticket has been booked! Your seat number is {self.seats}"
            )
            self.seats = self.seats - 1
        else:
            print("Sorry! this train is full")


a = Train("Karachi Express", 899, 300)
a.getStatus()
a.bookTicket()
a.getStatus()