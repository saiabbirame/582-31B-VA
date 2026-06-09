from users import Customer, Staff, VIPCustomer
from movie_show import MovieShow, InvalidBookingError, ShowSoldOutError, ShowCancelledError, InvalidStatusError
from status import ShowStatus

customer1 = Customer("Jane", "jane@gmail.com", "123456c")
staff1 = Staff("Carl", "carl@hotmail.com", "112233e")
vip1 = VIPCustomer("Peter", "peter@outlook.com", "135791v")

users = [customer1, staff1, vip1]

for user in users:
    user.display_info()

# Valid movie show
show1 = MovieShow("Obsession", 100, ShowStatus.OPEN)

show1.display_info()

# Valid tickets
show1.book_tickets(customer1, 8)

show1.display_info()

# Invalid tickets
try:
    show1.book_tickets(customer1, 20)

except InvalidBookingError as error:
    print("Error:", error)

# Invalid: Cancelled show
try:
    show2 = MovieShow("Devil Wears Prada 2", 150, ShowStatus.OPEN)

    show2.cancel_show()

    show2.book_tickets(customer1, 10)

except ShowCancelledError as error:
    print("Error:", error)

# Invalid: Sold Out show
try:
    show3 = MovieShow("Michael", 8, ShowStatus.OPEN)

    show3.book_tickets(customer1, 8)

    show3.display_info()

    show3.book_tickets(customer1, 2)

except ShowSoldOutError as error:
    print("Error:", error)

# Invalid capacity
try:
    show4 = MovieShow("Scary Movie 6", 0, ShowStatus.OPEN)

except ValueError as error:
    print("Error:", error)

# Invalid status
try:
    show5 = MovieShow("The Sheep Detectives", 10, "open")

except InvalidStatusError as error:
    print("Error:", error)
