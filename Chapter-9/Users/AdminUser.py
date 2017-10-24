"""Create a simple user class"""


class User():
    """Display complete details about given user"""

    def __init__(self, first_name, last_name):
        """Initial constructor"""

        self.first_name = first_name
        self.last_name = last_name
        self.login_attemps = 0

    def describe_user(self):
        """Describes as user information."""
        print("User Details")
        print("------------")
        print(f"Full Name :\t {self.first_name} {self.last_name}")
        print(
            f"Email: \t {self.first_name.lower()}."
            f"{self.last_name.lower()}@gmail.com")
        print()

    def increment_login_attempts(self, value):
        """Increments the login attempts of a single user."""
        if value < 1:
            pass
        else:
            self.login_attemps += 1

    def reset_login_attempts(self):
        """Resets the login attemps count to default"""
        self.login_attemps = 0


class Privileges():
    """Defining privileges class"""

    def __init__(self, privileges=['Can add post',
                                   'Can delete post', 'Can ban user']):
        self.privileges = privileges

    def show_privileges(self):
        """Lists all the privilges of the user."""
        print("Admin Roles")
        print("-----------")
        for i in self.privileges:
            print(i)


class Admin(User):
    """Defining admin user from user class"""

    def __init__(self, first_name, last_name):
        """Defining the super constructor"""
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


user_one = Admin("Naveen", "Mannam")

user_one.describe_user()
user_one.login_attemps
print(user_one.login_attemps)
user_one.increment_login_attempts(1)
user_one.privileges.show_privileges()
