# create a class of Fruit
    # give it 3 attributes
    # define 3 methods that access the attributes and return them
    # define a method that changes the price to a new price (taken as an parameter)
        # and returns the new price

class Fruit:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def get_name(self):
        return self.name
    
    def get_color(self):
        return self.color
    
    def get_price(self):
        return self.price
    
    def discounted_price(self):
        new_price = self.price - 0.20
        return new_price
    
fruit1 = Fruit("Apple", "Red", 1.50)
fruit2 = Fruit("Mango", "Yellow", 1.80)
fruit3 = Fruit("Banana", "Yellow", 2.40)

fruits = [fruit1, fruit2, fruit3]

print(fruit1.get_name())
print(fruit1.get_color())
print(fruit1.get_price())

fruit1_new_price = fruit1.discounted_price()
print(f"The discounted price is {fruit1_new_price}")

    
