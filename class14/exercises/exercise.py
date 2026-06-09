# 1
# Create a class with:
#   private balance
#   deposit(amount)
#   withdraw(amount)

# Use exceptions for:
#   negative deposit
#   negative withdrawal
#   insufficient funds

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit cannot be negative")
        
        self.__balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawal cannot be negative")
        
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        
        self.__balance -= amount

    def show_balance(self):
        print(f"Balance: {self.__balance}")

try:
    account = BankAccount(100)

    account.deposit(100)
    account.withdraw(50)

    account.show_balance()

except ValueError as error:
    print(error)

print()

# 2
# Create a class with:
#   property celsius


# Raise an exception if:
#   temperature is below absolute zero

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self.__celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        
        self.__celsius = value

try:
    temperature = Temperature(35)
    print(temperature.celsius)

    temperature.celsius = -300

except ValueError as error:
    print(error)

print()

# 3
# Create:
# class NegativePriceError(Exception):
#   pass

# Then use it in a Product class.

class NegativePriceError(Exception):
    pass

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise NegativePriceError("Price cannot be negative")
        
        self.__price = value

try:
    product = Product("Chair", 50)
    print(product.price)

    product.price = -20

except NegativePriceError as error:
    print(error)

