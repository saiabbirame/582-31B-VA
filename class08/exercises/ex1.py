# 1. identify visibility intent

class User:
    def __init__(self, username, email, password_hash):
        self.username = username # public
        self.__email = email # private
        self.__password_hash = password_hash # private

# which attributes are public? which are intended for internal use?


# 2. redesign the following class to improve encapsulation
class Course:
    def __init__(self, title, seats):
        self.title = title
        self.__seats = seats

    def add_seats(self, amount):
        if amount > 0:
            self.__seats += amount
        else:
            print("")