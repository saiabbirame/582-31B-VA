from book import Book

book1 = Book("The Cruel Prince", "Holly Black", True)
book2 = Book("Atomic Habits", "James Clear", False)

# PART2
print(book1.title)
print(book1.author)
print(book1.available)
print()

print(book2.title)
print(book2.author)
print(book2.available)
print()

# PART3
book1.display_info()
print()

book1.borrow()
book1.display_info()
print()

book1.return_book()
book1.display_info()
print()

book2.display_info()
book2.borrow()
print()

# PART4

