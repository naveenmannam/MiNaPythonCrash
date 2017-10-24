"""Car class module"""


class Car():
    """Car class"""

    def __init__(self, name, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.name = name
        self.miles = 0
        self.gas = 10

    def car_description(self):
        print("-----------")
        print("Car Details")
        print("-----------")
        print(f"Owner  :\t{self.name.title()}")
        print(f"Make   :\t{self.make.title()}")
        print(f"Model  :\t{self.model.title()}")
        print(f"Year   :\t{self.year}")
        print("-----------")

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

    def fill_gas_tank(self, lit):
        """Fills the gas tank of a car"""
        if lit <= 0:
            pass
        else:
            self.gas += lit
        print(f"{self.model} has {self.gas} litres of gas.")


class Battery():
    """Defining a battery class"""

    def __init__(self, battery_size=70):
        """Initial constructor"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery percentage."""
        print(
            f"This car has a battery "
            f"percentage of {self.battery_size}-kwh.")

    def upgrade_battery(self, battery_capacity=85):
        """Upgrades the battery capacity"""
        if self.battery_size < 85:
            self.battery_size = battery_capacity
            print("Battery has been upgraded tp 85-kwh.")
        elif self.battery_size >= 85:
            pass

    def get_range(self):
        """Defines the range of the vehice"""
        if self.battery_size == 70:
            print("Vehicle range is 240 Miles.")
        elif self.battery_size >= 85:
            print("Vehicle range is 270 Miles.")
        else:
            print("Check the battery.")


class ElectricCar(Car):
    """Deriving electric car from Car"""

    def __init__(self, name, make, model, year):
        """Initialise"""
        super().__init__(name, make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric car does not require gas"""
        print("Electric car does not require any gas.")
