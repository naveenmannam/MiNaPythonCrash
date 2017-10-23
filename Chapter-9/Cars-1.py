"""Car class"""


class Car():
    """Car class"""

    def __init__(self, name, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.name = name
        self.miles = 0

    def car_description(self):
        print("Car Details")
        print("-----------")
        print(f"Owner  :\t{self.name.title()}")
        print(f"Make   :\t{self.make.title()}")
        print(f"Model  :\t{self.model.title()}")
        print(f"Year   :\t{self.year}")
        print()

    def update_ode(self, mileage):
        if mileage >= self.miles:
            self.miles = mileage
        else:
            pass

    def increment_ode(self, miles):
        if miles < 0:
            pass
        else:
            self.miles += miles

    def odo_reading(self):
        print(
            f"{self.name.title()}'s car "
            f"{self.model.title()} ODO meter reading : {self.miles}")
        print()
        print()


car_1 = Car("Naveen", "Honda", "Civic", '2013')
# car_2 = Car("Pavan", "Honda", "Accord", '2006')
# car_3 = Car("Venki", "Honda", "SUV", '2017')

car_1.car_description()
car_1.odo_reading()
car_1.update_ode(20)
car_1.odo_reading()
car_1.increment_ode(-3)
car_1.update_ode(15)
car_1.odo_reading()
car_1.increment_ode(23)
car_1.odo_reading()
