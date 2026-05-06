# Exercise 1
class Book:
    book_count = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.book_count += 1

book1 = Book("The Cruel Prince", "Holly Black")
book2 = Book("Final Offer", "Lauren Asher")
book3 = Book("An Offer From A Gentleman", "Julia Quinn")

print(f"Books added: {Book.book_count}")

# Exercise 2
class Student:
    school_name = "Vanier College"
    student_count = 0

    def __init__(self, name, program, grade):
        self.name = name
        self.program = program
        self.grade = grade
        Student.student_count += 1

    def display_info(self):
        print(f"{self.name} studies {self.program} at {self.school_name}. Grade: {self.grade}")

student1 = Student("Josh", "Architecture", 88)
student2 = Student("Matt", "Computer Science", 92)
student3 = Student("Leila", "Communication", 89)
student4 = Student("Max", "Graphic Design", 90)

student1.display_info()
student2.display_info()
student3.display_info()
student4.display_info()

print(f"Number of students created: {Student.student_count}")

# Exercise 3
class Product:
    category = "Electronics"
    tax_rate = 0.15

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def price_with_tax(self):
        return self.price + (self.price * self.tax_rate)
    
product1 = Product("Monitor", 250)
product2 = Product("Speaker", 125)
product3 = Product("Touchpad", 170)

print(f"Price with tax for {product1.name} is: {product1.price_with_tax()}")
print(f"Price with tax for {product2.name} is: {product2.price_with_tax()}")
print(f"Price with tax for {product3.name} is: {product3.price_with_tax()}")

Product.tax_rate = 0.20

print("After changing tax rate to 0.20:")
print(f"Price with tax for {product1.name} is: {product1.price_with_tax()}")
print(f"Price with tax for {product2.name} is: {product2.price_with_tax()}")
print(f"Price with tax for {product3.name} is: {product3.price_with_tax()}")

# Exercise 4
class Employee:
    company_name = "TechNova"
    bonus_rate = 0.10
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def calculate_bonus(self):
        return self.salary * self.bonus_rate
    
    def display_employee(self):
        print(f"{self.name} works at {self.company_name}. Salary: {self.salary}. Bonus: {self.calculate_bonus()}")

employee1 = Employee("John", 50000)
employee2 = Employee("Paul", 35000)
employee3 = Employee("Sarah", 65000)

print(f"Number of employees created: {Employee.employee_count}")

print("All employees:")
employee1.display_employee()
employee2.display_employee()
employee3.display_employee()

Employee.bonus_rate = 0.20

print("After changing bonus rate to 0.20:")
employee1.display_employee()
employee2.display_employee()
employee3.display_employee()

employee1.bonus_rate = 0.50

print("After giving employee #1 a custom bonus rate:")
employee1.display_employee()
employee2.display_employee()
employee3.display_employee()

Employee.bonus_rate = 0.05

print("After changing bonus rate to 0.05:")
employee1.display_employee()
employee2.display_employee()
employee3.display_employee()

# employee1 has a shadowed bonus_rate because we created its own bonus rate when writing:
# employee1.bonus_rate = 0.50 
# we created a new instance attribute on employee1, just like the example we saw in class