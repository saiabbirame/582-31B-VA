class Book:
    def __init__(self, title, author, available = True):
        self.title = title
        self.author = author
        self.available = available

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Available: {self.available}")