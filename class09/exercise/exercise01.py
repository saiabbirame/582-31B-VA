# Ex.1

# Create a class with:
#   name
#   private __gpa
# Requirements:
#   property gpa
#   setter only accepts values between 0.0 and 4.0

class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.__gpa = gpa

    @property
    def gpa(self):
        return self.__gpa
    
    @gpa.setter
    def gpa(self, value):
        if value >= 0.0 and value <= 4.0:
            self.__gpa = value
        else:
            print("Invalid GPA")

student1 = Student("Jane", 3.2)

print(student1.gpa)

student1.gpa = 3.5
print(student1.gpa)

student1.gpa = 4.5

print()

# Ex.2

# Create a class with:
#   name
#   internal _price
# Requirements:
#   property price

# setter must reject negative values

class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            print("Price cannot be negative")

product1 = Product("Monitor", 250)

print(product1.price)

product1.price = 180
print(product1.price)

product1.price = -20

print()

# Ex.3 

# Create a class with:
#   radius

# Requirements:
# a read-only property area

# You should not store area directly; you should compute it.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius * self.radius
    
circle1 = Circle(5)

print(circle1.area)

print()

# Ex.4 

# Create a class with:
#   first_name
#   last_name
# Requirements:
#   read-only property full_name

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
person1 = Person("Alice", "Clark")

print(person1.full_name)

print()

# Ex.5

# Create a class with:
#   owner
#   private __balance
# Requirements:
#   property balance
#   setter prevents negative values
#   method deposit(amount)
#   method withdraw(amount)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        if value >= 0: 
            self.__balance = value
        else:
            print("Balance cannot be negative")

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

account1 = BankAccount("Mark", 200)

print(account1.balance)

account1.deposit(300)
print(account1.balance)

account1.withdraw(150)
print(account1.balance)

account1.withdraw(500)

print()

# Ex.6

# Create a class with:
#   name
#   private __price
#   quantity
# Requirements:
#   property price
#   setter prevents negative values
#   read-only property inventory_value

class Inventory:
    def __init__(self, name, price, quantity):
        self.name = name
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value >= 0:
            self.__price = value
        else:
            print("Invalid price")

    @property
    def inventory_value(self):
        return self.__price * self.quantity
    
item1 = Inventory("Pen", 6, 28)

print(item1.price)
print(item1.inventory_value)

item1.price = 9

print(item1.inventory_value)

print()

# Ex.7

# Create a class with:
#   title
#   private __rating
# Requirements:
#   property rating
#   setter only accepts values between 0 and 10

class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.__rating = rating

    @property
    def rating(self):
        return self.__rating
    
    @rating.setter
    def rating(self, value):
        if value >= 0 and value <= 10:
            self.__rating = value
        else:
            print("Invalid rating")

movie1 = Movie("Smile", 8)

print(movie1.rating)

movie1.rating = 7.5
print(movie1.rating)

movie1.rating = 15