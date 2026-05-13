from abc import ABC, abstractmethod
# 1. Create an abstract class:
# Vehicle
# abstract method: move()

# Create subclasses:
# Car
# Bicycle

# Each must implement move() differently.

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("The car is moving.")

class Bicycle(Vehicle):
    def move(self):
        print("The bicycle is moving.")

car1 = Car()
bicycle1 = Bicycle()

car1.move()
bicycle1.move()
print()

# 2. Create an abstract class:
# FileHandler
# abstract methods: 
# read()
# write()

# Create subclasses:
# TextFileHandler
# JsonFileHandler

# They can just print messages instead of reading real files.

class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

class TextFileHandler(FileHandler):
    def read(self):
        print("Reading text file")

    def write(self):
        print("Writing text file")

class JSONFileHandler(FileHandler):
    def read(self):
        print("Reading JSON file")

    def write(self):
        print("Writing JSON file")

text_file = TextFileHandler()
json_file = JSONFileHandler()

text_file.read()
text_file.write()

json_file.read()
json_file.write()
print()

# 3. Create an abstract class:
# Account
# abstract method: calculate_fee()

# Create subclasses:
# SavingsAccount
# PremiumAccount

# Each returns a different fee.

class Account(ABC):
    @abstractmethod
    def calculate_fee(self):
        pass

class SavingsAccount(Account):
    def calculate_fee(self):
        return 10
    
class PremiumAccount(Account):
    def calculate_fee(self):
        return 25
    
savings = SavingsAccount()
premium = PremiumAccount()

print(f"Savings fee: ${savings.calculate_fee()}")
print(f"Premium fee: ${premium.calculate_fee()}")
print()

# 4. abstract Employee
# Create:
# abstract class Employee
# abstract method calculate_salary()

# Subclasses:
# FullTimeEmployee
# PartTimeEmployee

# Each should calculate salary differently.

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, monthly_rate):
        self.monthly_rate = monthly_rate

    def calculate_salary(self):
        return self.monthly_rate
    
class PartTimeEmployee(Employee):
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        return self.hours * self.rate
    
full_time = FullTimeEmployee(6000)
part_time = PartTimeEmployee(25, 16.50)

print(f"Full-Time Salary: ${full_time.calculate_salary()}")
print(f"Part-Time Salary: ${part_time.calculate_salary()}")
print()

# 5. abstract Media
# Create:
# abstract class Media
# abstract method play()

# Subclasses:
# Song
# Video

# Each implements play() differently.

class Media(ABC):
    @abstractmethod
    def play(self):
        pass

class Song(Media):
    def play(self):
        print("Playing a song")

class Video(Media):
    def play(self):
        print("Playing a video")

song1 = Song()
video1 = Video()

song1.play()
video1.play()