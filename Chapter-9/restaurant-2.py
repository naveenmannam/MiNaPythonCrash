""" Simple Restaurant Class """


class Restaurant():
    """Restaurant class"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initial Constructor"""
        self.rest_name = restaurant_name
        self.cuis_type = cuisine_type

    def describe_restaurant(self):
        """Describe in-detail about the restaurant."""
        print(f"{self.rest_name} is a well "
              f"established {self.cuis_type} restaurant.")
        print(f"You will love the food, its delicious.")

    def open_restaurant(self):
        """Displays message that the restaurant is open"""
        print(f"{self.rest_name} is now open.")


restaurant_1 = Restaurant("Michnaro", "Chinese")
restaurant_2 = Restaurant("Saravana", "Indian")
restaurant_3 = Restaurant("Pasta Palace", "Italian")
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
