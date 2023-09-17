from car_inventory import track

class Customer:
    """Customer class of the Carxify program. It calls the methods
    for customers in making a rent request and returning a rented car ."""

    def requestToRent(self):
        """Creates the customer request to rent a car from the inventory"""

        print("\nWelcome to our car renting platform!")
        self.cars = str(input("Please confirm the car you want to rent: \n"
                         "Type(Sedan, Hatchback or SUV?)\n>>>>>: "))
        return self.cars.title()

    def returnRentedCar(self):
        """Returns the rented car to the inventory"""

        print("Thanks for attempting a return.")
        name = input("Enter your name: ")
        print("What car would you like to return?")
        self.car = input("Sedan/Hatchback/SUV\n>>>>>:  ")
        if {name.title(): self.car.title()} in track:
            track.remove({name.title(): self.car.title()})
            return self.car.title()
        else:
            print("Wrong name/car!\nPlease try again!")
            exit()




