class Book:
    library_name = "Central Library"

    def __init__(self, title, author, available = True):
        self.title = title
        self.author = author
        self.available = available

    def display_info(self):
        print(f"{self.title} by {self.author} is Available: {self.available}")

    def borrow(self):
        if (self.available == False):
            print(f"{self.title} is already borrowed.")
        else: 
            self.available = False
            print(f"{self.title} has been borrowed.")

    def return_book(self):
        self.available = True
        print(f"{self.title} has been returned.")

    @classmethod
    def change_library_name(cls, new_name):
        cls.library_name = new_name

    @staticmethod
    def is_valid_title(title):
        if(len(title.strip()) > 0):
            return True
        else:
            return False