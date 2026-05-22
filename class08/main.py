# encapsulation

class Book:
    def __init__(self, name):
        self.name = name

book1 = Book("test")

book1.name = "something else"

print(book1.name)

# public -- data can be accessed from anywhere (inside or outside)
# private -- protects the data from being accessed DIRECTLY outside of the class.
#   ex: private name


# in Python, we only use naming conventions and developer responsibility

# Python trusts the programmer more
# visibility (public, private) is about communication and design, not just compiler-enforced rules!


# so far we've seen:

# classes
# instance attr.
# instance methods
# class attr.
# class methods
# static methods
# abstraction and interfaces

# let's bring in encapsulation here:

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

acc1 = BankAccount("Alice", 500)
acc1.balance = -1000

# we need to protect our code from ourselves!

# encapsulation means keeping data and the rules for using that data together inside the class.
# it also means:
#               limiting direct access to internal details
#               protecting object state from invalid changes
#               exposing a cleaner public interface


# we want our class to help control how that data is used.


# ============

# we have three naming patterns to signal intended visibility

# 1. public
name = "hi"

# a poorly encapsulated class
class Student:
    def __init__(self, name):
        self.name = name

student1 = Student("John")
student1.name = "Ali"
# ^ this is a public attribute

# 2. private
__name = "hi"

class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.__gpa = gpa # private attr.

student2 = Student("Alice", 3.8)
# print(student2.__gpa) # this would fail, because of the concept of name mangling



# 3. protected
_name = "hi"


# what is name mangling?

# when an attribute starts with __ inside a class, Python changes its internal name to reduce accidental
# access and accidental overriding.

student3 = Student("Jane", 3.5)
print(student3.__dict__) 
# ^ we see that __gpa has been transformed to _Student__gpa internally.

print(student3._Student__gpa)
# print(student3.__gpa) # this doesn't show anything and throws an error

# the goal of using this private accessor is to 
#   avoid accidental direct access

# poorly encapsulated example
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

print("===================")
# how can we design it in a better encapsulated way?
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance # private!
        # __balance is signaling internal use! within the class itself

    # the following methods will handle data internally
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def show_balance(self):
        print(f"Balance is: {self.__balance}")

bank_account1 = BankAccount("Jane", 500)
# bank_account1.__balance = 1000 # this would throw an error

# the method is handling the interaction
bank_account1.deposit(500) # deposit() handles data internally!
bank_account1.show_balance() # show_balance() accesses data internally and then shows us!
bank_account1.withdraw(200) # withdraw handles data internally
bank_account1.show_balance() # show_balance() accesses data internally and then shows us!

# why is this better?
#   rules are handled through methods
#   raw external data mutation/change is prohibited!


# one more example!

class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    def set_celsius(self, value):
        if value >= -273: # we're protecting our data!
            self.__celsius = value
        else:
            print("Invalid temperature!")

    def show_celsius(self):
        print(f"{self.__celsius} C")

temp1 = Temperature(8)
temp1.set_celsius(23)
temp1.show_celsius()