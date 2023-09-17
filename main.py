"""
Project: Car rental system called "Carxify"
"""
from car_inventory import CarInventory, track
from customer import Customer
from vip_customer import VipCustomer


#Create object of the class CarInventory
Carxify = CarInventory({
    "Sedan": 4,
    "Hatchback": 3,
    "Suv": 3
})
#Create object of the class Customer, VipCustomer and VIPCarI
customer = Customer()
vip_customer = VipCustomer()

print("""
*****************************************************************
  ______     ___      .______     ___   ___  __   ___________    ____ 
 /      |   /   \     |   _  \    \  \ /  / |  | |   ____\   \  /   / 
|  ,----'  /  ^  \    |  |_)  |    \  V  /  |  | |  |__   \   \/   /  
|  |      /  /_\  \   |      /      >   <   |  | |   __|   \_    _/   
|  `----./  _____  \  |  |\  \----./  .  \  |  | |  |        |  |     
 \______/__/     \__\ | _| `._____/__/ \__\ |__| |__|        |__|   
 *****************************************************************
    \t\t\tYour online car renting platform\t\t\t\t
    """)
while True:
    print("*****************************************************************\n"
        "1. View available cars.\n2. Rent a car \n3. Return a rented Car. "
        "\n4. View rented cars \n5. Exit")
    try:
        choice = int(input("\tPress enter your choice \n\t>>>>>: "))

        if choice == 1:                 # Produces all available cars in the inventory
            Carxify.viewCars()
        elif choice == 2:               # Allows user rent a car
            print("Do you have a loyalty card? ")
            choice = input("Enter 'Y' for Yes and 'N' for No.\n>>>>>: ")
            if choice.upper() == 'Y':
                Carxify.VipRenter(
                    input("Please enter your name:\n>>>>> "),
                    int(input("How many days would you like to rent the car for?\n>>>>>: ")),
                    vip_customer.requestToRent()
                )
            elif choice.upper() == 'N':
                Carxify.rentOutCar(
                    input("Please enter your name:\n>>>>> "),
                    int(input("How many days would you like to rent the car for?\n>>>>>: ")),
                    customer.requestToRent()
                )
            else:
                print("Please enter only 'Y' or 'N'!")
        elif choice == 3:               #Returns rented car
            Carxify.returnCar(
                int(input("How many days have you rented the car for? ")),
                customer.returnRentedCar())

        elif choice == 4:               #Tracks all rented cars
            """As this is an Admin function, it requires password to access it
             Password has been set to 'Digital123' """

            print("Please enter password: ")
            password = input(">>>>>: ")
            if password == "Digital123":
                for i in track:
                    for key, value in i.items():
                        renter = key
                        type_of_car = value
                        print(f"\n{renter} has rented a {type_of_car} car")
                print("\n")
                if len(track) == 0:
                    print("We have a full inventory, no cars have been rented out!\n")
            else:
                print("You have entered the wrong password")
                print("Remember! This is an admin function")


        elif choice == 5:               #To exit
            print("Thanks for using our service\n")
            exit()
        else:
            print("Invalid input")
    except Exception as e:  # catch errors
        print(f"{e}---> INVALID INPUT! \n")


