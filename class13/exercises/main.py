# 1
# Create a parent class:

#   Animal
#   method: speak()

# then child classes:
#   Dog
#   Cat

# Override speak in ceach child!

# Dog says "Woof"
# Cat says "Meow"

# Then loop through them polymorphically

class Animal:
    def speak(self):
        print("Animal says")

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

animals = [
    Dog(),
    Cat()
]

for animal in animals:
    animal.speak()

# 2
# Create a parent class: Vehicle
# Child classes Car and Bike

# they share:
# brand
# describe()

# add child-specific behaviour

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def describe(self):
        print(f"Brand: {self.brand}")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def start(self):
        print(f"{self.model} is starting")

class Bike(Vehicle):
    def __init__(self, brand, bike_type):
        super().__init__(brand)
        self.bike_type = bike_type

    def ride(self):
        print(f"Riding a {self.bike_type} bike")

car = Car("Mitsubishi", "Lancer")
bike = Bike("Trek", "Mountain")

car.describe()
car.start()

bike.describe()
bike.ride()

# 3
# parent class: Account
#               show_type()

# children accounts: SavingsAccount & PremiumAccount
#   override or extend behaviour accordingly

class Account:
    def show_type(self):
        print("Generic Account")

class SavingsAccount(Account):
    def show_type(self):
        print("Savings Account")

class PremiumAccount(Account):
    def show_type(self):
        print("Premium Account")

# If extend:

# class PremiumAccount(Account):
#     def show_type(self):
#         super().show_type()
#         print("Includes benefits")

accounts = [
    SavingsAccount(),
    PremiumAccount()
]

for account in accounts:
    account.show_type()


