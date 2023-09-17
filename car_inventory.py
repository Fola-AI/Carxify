
class CarInventory:
    def __init__(self, list_of_cars):
        """Function that initializes to the carxify Car library"""
        self.car = list_of_cars

    def viewCars(self):
        """Function to view all available cars in the Carxify inventory"""

        print(f"We have the following cars available for rent:")
        total = 0
        for cars, value in self.car.items():
            print(cars, value, sep=": ")
            total += value
        print(f"Total cars available: {total}\n")

    def rentOutCar(self, name, days, car_type):
        """Function to rent out cars"""

        if car_type not in self.car:     #carType was returned from function "requestToRent" from the Customer class
            print("Your input was not found in cars available for rent! ")
        else:
            car_type in self.car
            for key, value in self.car.items():
                if self.car[key] == 0:
                    print(f"{car_type} has 0 cars in the inventory")
                    print("Please check available cars and try again ")
                    exit()

            charge = ""
            if car_type == "Sedan":  # If selection is Sedan
                if days <= 0:
                    print("Minimum rent days is 1")
                elif days > 0 and days <= 6:
                    charge = (days * 50)
                else:
                    charge = (days * 40)
            elif car_type == "Hatchback":  # If selection is Hatchback
                if days <= 0:
                    print("Minimum rent days is 1")
                elif days > 0 and days <= 6:
                    charge = (days * 30)
                else:
                    charge = (days * 25)
            elif car_type == "Suv":  # If selection is SUV
                if days <= 0:
                    print("Minimum rent days is 1")
                elif days > 0 and days <= 6:
                    charge = (days * 100)
                else:
                    charge = (days * 90)

            print("\n**************************************************")
            print(f"You have rented a {car_type} car for {days} days. "
                  f"\nYou will be charged £{charge} for {days} days. \n")
            print("We hope that you enjoyed our service.")

            track.append({name.title(): car_type})
            for key, value in self.car.items():
                if key == car_type:
                    value -= 1
                    self.car[car_type] = value  # Update the library with updated value

    def VipRenter(self, name, days, car_type):
        """VipRenter is a method for rates of VIP/Loyalty customers
                 VIP rate/day -
                 Sedan: £35
                   Hatchback: £20
                   SUV: £80
             """

        if car_type not in self.car:     #carType was returned from function "requestToRent" from the Customer class
            print("Your input was not found in cars available for rentssssss! ")
        else:
            car_type in self.car
            for key, value in self.car.items():
                if self.car[key] == 0:
                    print(f"{car_type} has 0 cars in the inventory")
                    print("Please check available cars and try again ")
                    exit()

            charge = ""
            if car_type == "Sedan":         # Sedan rate is £20 for VIP customers
                if days <= 0:
                    print("Minimum rent days is 1")
                else:
                    charge = (days * 35)
            elif car_type == "Hatchback":  # Hatchback rate is £20 for VIP customers
                if days <= 0:
                    print("Minimum rent days is 1")
                else:
                    charge = (days * 20)
            elif car_type == "Suv":         # SUV rate is £20 for VIP customers
                if days <= 0:
                    print("Minimum rent days is 1")
                else:
                    charge = (days * 80)
            else:
                print("Invalid input")
                exit()

            print("\n**************************************************")
            print(f"You have rented a {car_type} car for {days} days. "
                  f"You will be charged £{charge} for {days} days. \n")
            print("We hope that you enjoyed our service.")

            track.append({name.title(): car_type})
            for key, value in self.car.items():
                if key == car_type:
                    value -= 1
                    self.car[car_type] = value  # Update the library with updated value

    def returnCar(self, days, car_type):
        charge = ""
        if car_type == "Sedan":  # If selection is Sedan
            if days <= 0:
                print("Minimum rent days is 1")
            elif days > 0 and days <= 6:
                charge = (days * 50)
            else:
                charge = (days * 40)
        elif car_type == "Hatchback":  # If selection is Hatchback
            if days <= 0:
                print("Minimum rent days is 1")
            elif days > 0 and days <= 6:
                charge = (days * 30)
            else:
                charge = (days * 25)
        elif car_type == "Suv":  # If selection is SUV
            if days <= 0:
                print("Minimum rent days is 1")
            elif days > 0 and days <= 6:
                charge = (days * 100)
            else:
                charge = (days * 90)
        else:
            print("Invalid input")
            exit()

        print(f"\nYou have returned a {car_type} car after renting for "
              f"a period of {days} days.\nYour total bill is £{charge}")
        print("Thanks for using our service!\n")
        for key, value in self.car.items():
            if key == car_type:
                value += 1
                self.car[car_type] = value


track = []          #Keeps record as follows - {car renter: type of car rented}


