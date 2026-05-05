# Let's create a class for a book

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

book1 = Book("100 Years of Solitude", "Gabriel Garcia Marquez", 10.99)
book2 = Book("Clean Code", "Robert C. Martin", 20.99)

print(book1.price) # we should see 10.99

# we can overwrite the property
book1.price = 100.99

print(book1.price) # we should see 100.99

class Product:
    # default argument treats it as 'optional'
    # in a sense that if you don't get any values for it
    # it just assigns the default value
    def __init__(self, name, price = 0, stock = 0):
        self.name = name
        self.price = price
        self.stock = stock

p1 = Product("Keyboard", 20, 10)
p2 = Product("Mouse", 5) # I don't want to put stock here
print(p2.stock)

p2.stock = 100
print(p2.stock)

p3 = Product("Banana", stock = 10, price = 20) # positional argument
p4 = Product(name = "Cherry", price = 10, stock = 5)

# the moment we introduce positional keywords, all the following arguments need to follow that same format