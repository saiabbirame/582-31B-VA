# Class attributes VS Instance attributes

class Student:
    def __init__(self, name, program):
        self.name = name
        self.program = program

student1 = Student("Alice", "Web Development")
student2 = Student("Karim", "Computer Science")

print(student1.name)
print(student2.name)

# what if all students were from the same school?

# the idea is:
    # some data belongs to:
    #   each object individually
    # Other data belongs to:
    #   the whole class

# instance attribute --> per-object state
# class attribute --> shared class-level state

class Student:
    school_name = "Vanier College" # This is our shared class attribute

    def __init__(self, name, program):
        # these are instance attributes / per-object state
        self.name = name
        self.program = program

student1 = Student("Alice", "Web Development")
student2 = Student("Karim", "Computer Science")

print(student1.name)
print(student2.name)

print(student1.school_name)
print(student2.school_name)

Student.school_name = "ABC College" # we can change the shared attribute directly for all instances of a class
print('----')
print(student1.school_name)
print(student2.school_name)

# visual comparison:

    # Instance attributes:
    #   created with self
    #   usually set in __init
    #   different per object

    # Class attributes:
    #   defined in class body
    #   shared across all instances
    #   used for common data or class-level configuration
print('----')
class Product:
    category = "Electronics" # shared

    def __init__(self, name, price):
        self.name = name # per object
        self.price = price # per object

product1 = Product("Keyboard", 10)
product2 = Product("Mouse", 25)

product1.price = 8

print(product1.price)
print(product2.price)
print(product1.category)
print(product2.category)


# shadowing a class attribute
print('-----')
class Employee:
    bonus = 0.5 # this is a class attribute

    def __init__(self, name):
        self.name = name # this is an instance attribute

employee1 = Employee("John")
employee2 = Employee("Jane")

print(f"Employee 1 Bonus: {employee1.bonus}") # 0.5
print(f"Employee 2 Bonus: {employee2.bonus}") # 0.5

Employee.bonus = 1 # change class attribute globally

print(f"Employee 1 Bonus: {employee1.bonus}") # 1
print(f"Employee 2 Bonus: {employee2.bonus}") # 1

employee1.bonus = 2 # changing the shadow attribute
                    # this doesn't change the class attribute itself!
                    # we create a new instance attribute on employee1!

employee3 = Employee("test")

print(f"Employee 1 Bonus: {employee1.bonus}") # 2
print(f"Employee 2 Bonus: {employee2.bonus}") # 1
print(f"Employee 3 Bonus: {employee3.bonus}") # 1

Employee.bonus = 0.5 # change class attribute globally back to 0.5

print(f"Employee 1 Bonus: {employee1.bonus}") # 2
print(f"Employee 2 Bonus: {employee2.bonus}") # 0.5
print(f"Employee 3 Bonus: {employee3.bonus}") # 0.5

# the process above is shadowing
# we are creating a new instance attribute based on a class attribute.


# case study

# Good use cases for class attributes are :
    # shared across all instances
    # conceptually the same for the whole class
    # they're usually configuration-like or constant-like
    # they're counters or class-wide metadata

# Bad use cases for class attributes are :
    # values that should usually be differented per object.
    # any value that changes often, or is individually different

# let's look at some examples:
    # school name --> class attribute
    # max capacity --> class attribute 
    # account password --> instance attribute
    # tax rate --> class attribute
    # course grade --> instance attribute