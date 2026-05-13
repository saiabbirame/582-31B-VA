# Interfaces / Abstraction

# so far we've built concrete classes 

class Book:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Book name is: {self.name}")

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Product name is {self.name}")


# let's move one level higher than just concrete classes.

# instead of asking what one object does, we ask what a whole category of objects should be able to do.


# in the examples above, we see that our classes might behave in a similar way and we want to think of 
# abstraction as a way that allows us to design our code.

# in here, abstraction means focusing on the essential behaviour, while hiding unnecessary details.


# Imagine a payment system --> every payment method must have a pay(amount) operation

# but!!    a credit card pays one way -- PayPal pays another way -- bank transfer works differently , etc.

# the shared  idea for the above:  is the abstraction "a payment method can make a payment"

# abstraction allows us to have 
# 1. clearer design
# 2. less duplication
# 3. easier extension
# 4. more consistent behaviour
# 5. in case of larger code bases: better teamwork and maintainability

# let's get practical now!

# the common approach to use interfaces in python is :
# abstract base classes using the abs module

# 1. import interfaces module 
from abc import ABC, abstractmethod

# ABSTRACT CLASS Shape
class Shape(ABC): # ABC means this class is abstract
    @abstractmethod # we mark a method that subclasses must implement
    def area(self):
        pass

# VERY IMPORTANT: Shape on its own cannot and must not be instantiated directly.

# shape = Shape()

class Rectangle(Shape): # Implements Abstract class SHAPE
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    # MUST define area(), otherwise it throws an error
    def area(self): 
        return self.width * self.height
    
class Circle(Shape): # Implements Abstract class SHAPE
    def __init__(self, radius):
        self.radius = radius

    # MUST define area(), otherwise it throws an error
    def area(self):
        return 3.14 * self.radius * self.radius

# here we see that both classes implement the abstract class SHAPE and its methods, but in their own way.
# every Shape must provide an area() method

rectangle = Rectangle(2, 4)
circle = Circle(3)

print(f"Rectangle's area is : {rectangle.area()}")
print(f"Circle's area is : {circle.area()}")

print("====================")
# this could be the code that interacts with our classes
def print_area(shape):
    print(shape.area())

print_area(rectangle)
print_area(circle)

# another example

# This is our CONTRACT
class FinancialInstitution(ABC):
    @abstractmethod
    def payment(self, amount):
        pass

class Visa(FinancialInstitution):
    def __init__(self, card_number):
        self.card_number = card_number
        self.balance = 0

    def payment(self, amount):
        self.balance += amount
        print(f"{amount} withdrawn! by Visa")

    def show_balance(self):
        print(self.balance)

class PayPal(FinancialInstitution):
    def __init__(self, card_number, debit_balance):
        self.card_number = card_number
        self.debit_balance = debit_balance

    def payment(self, amount):
        self.debit_balance -= amount
        print(f"{amount} paid by Paypal!")

    def donate(self):
        pass

visa_card = Visa("123")
tam_paypal_account = PayPal("456", 100)
kamyar_paypal_account = PayPal("45642624", 100)

print("===========")
def checkout(amount, fi):
    print(f"You owe ${amount}")

    fi.payment(amount)

checkout(50, tam_paypal_account)



# another example


# i want to have multiple animal classes (dog, cat, etc.)
# i want them all to be able to speak

class Animal(ABC): #Abstract Base Class
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    # we don't really need a constructor for now
    voice = "Woof"

    def speak(self):
        print(f"{self.voice}")

class Cat(Animal):
    def speak(self):
        print("Meow")

dog1 = Dog()
cat1 = Cat()

# this is valid
dog1.speak()
cat1.speak()

# this is not a must
# this is a choice
#                        this is also valid!
def animal_sound(animal):
    animal.speak()

animal_sound(dog1)
animal_sound(cat1)

# With abstraction:
# 1. The design is clearer (it's intentional!)
# 2. subclasses are required to implement the method
# 3. the shared purpose is explicit!


# Abstraction is good when:
#   when several classes must follow the same contract
#   when there's shared behaviour
#   when we want consistency

# Abstraction is overkill when:
#   when there's no need for shared contract
#   for small one-off classes (specific classes that only do one thing)
