class Book:
    library_name = "Central Library"

    def __init__(self, title, author, available = True):
        self.title = title
        self.author = author
        self.available = available

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Available: {self.available}")

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

   