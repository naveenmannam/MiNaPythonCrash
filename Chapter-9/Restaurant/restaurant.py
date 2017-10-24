""" Simple Restaurant Class module"""


class Restaurant():
    """Restaurant class"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initial Constructor"""
        self.rest_name = restaurant_name
        self.cuis_type = cuisine_type
        self.cust_served = 0

    def describe_restaurant(self):
        """Describe in-detail about the restaurant."""
        print(f"{self.rest_name} is a well established "
              f"{self.cuis_type} restaurant.")
        print(f"You will love the food, its delicious.")

    def set_customer_served(self, cust):
        if cust >= self.cust_served:
            self.cust_served = cust
        else:
            pass

    def customers_served(self):
        """Returns the number of customers server"""
        print(f"{self.cust_served} customers are been served as of now.")

    def increment_customers(self, cust):
        """Increment the number of customers served"""
        if cust <= 0:
            pass
        else:
            self.cust_served += cust

    def open_restaurant(self):
        """Displays message that the restaurant is open"""
        print(f"{self.rest_name} is now open.")


class Icecream(Restaurant):
    """Super class restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Creating the child constructor"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Vanila', 'Pista', 'Mango', 'Strawberry', 'Blueberry']

    def display_flavors(self):
        """Displays all the available flavors"""
        print("Availble Ice cream flavors.")
        for i in self.flavors:
            print(i)
