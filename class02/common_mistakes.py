# some common bugs!!

# 1
class Student:
    def __init__(name, program): # in this case, we miss self in the argument!
        self.name = name
        self.program

# 2
class Friend:
    # initialize
    # Here, we NEED to put the default argument(s) at the end
    # so the code doesn't get confused with the order of arguments.
    # In this case: this wouldn't compile at all!
    # Error: Non-default argument follows default argument
    def __init__(self, name, last_name = None, age, hobby):
        self.name = name
        self.last_name = last_name
        self.full_name = name + " " + last_name # for example, if the name Jane and last name is Doe, full name would be Jane Doe
        self.age = age
        self.hobby = hobby

f1 = Friend("Evgeniya", 29, "Coding")

# 3
class Student:
    def __init__(self, name, program):
        # Without self.name (or program) we're not storing the data to this object at all
        # (we're storing nothing actually)
        name = name
        program = program

# 4
student = Student("a", "b")
Student.name # this is not referring to our created object! CASE SENSITIVE

# 5
# INDENTATION!!!
class Friend:
    def __init__(self, name, last_name, age, hobby):
    # WRONG!
    # Properties need to be inside the init function!!
    self.name = name
    self.last_name = last_name
    self.full_name = name + " " + last_name
    self.age = age
    self.hobby = hobby
        
    def print_info(self):
        print(self.name, self.age, self.hobby)

        # WRONG! FUNCTION GREET IS ITS OWN THING!
        # You would need to put it at the right place (shift to the left)
        def greet(self):
            print("Hello!", self.name, "How are you?")

    # WRONG!
    # the variable needs to be outside of the class
    friend = Friend("a", "b", "c", "D")