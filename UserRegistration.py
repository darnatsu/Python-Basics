
class UserRegistration:
    def __init__(self, first_name, last_name, full_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = full_name
        self.email = email

user = UserRegistration("Darryl", "Diapolet", "Darryl Diapolet", "dar.diapolet@gmail.com")


print("My first name is {}." . format(user.first_name))