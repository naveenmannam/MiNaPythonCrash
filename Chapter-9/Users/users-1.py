"""Create a simple user class"""


class User():
    """Display complete details about given user"""

    def __init__(self, first_name, last_name):
        """Initial constructor"""

        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("User Details")
        print("------------")
        print(f"Full Name :\t {self.first_name} {self.last_name}")
        print(
            f"Email: \t {self.first_name.lower()}.{self.last_name.lower()}@gmail.com")
        print()


user_one = User("Naveen", "Mannam")
user_two = User("Minny", "Mannam")
user_three = User("Rohisuhas", "Kancharla")

user_one.describe_user()
user_two.describe_user()
user_three.describe_user()
