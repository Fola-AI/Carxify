from customer import Customer


class VipCustomer(Customer):
    """VIPCustomer class inheriting all of parents class methods and properties
    The requestToRent and returnRentedCar function from the parent class are both inherited,
     however, we define new parameters for the rentOutCar function due to a change in price
     VIP rate/day:
        Sedan: £35
        Hatchback: £20
        SUV: £80
    """
    def requestToRent(self):
        super().requestToRent()
        return self.cars.title()

    def returnRentedCar(self):
        super().returnRentedCar()