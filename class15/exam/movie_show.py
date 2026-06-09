from constants import MAX_TICKETS_PER_BOOKING
from status import ShowStatus

class InvalidBookingError(Exception):
    pass

class ShowSoldOutError(Exception):
    pass

class ShowCancelledError(Exception):
    pass

class InvalidStatusError(Exception):
    pass

class MovieShow:
    def __init__(self, title, capacity, status):
        if not title.strip():
            raise ValueError("Title cannot be empty")
        
        self.__title = title

        self.__capacity = 1
        self.__booked_seats = 0
        self.__status = ShowStatus.OPEN

        self.capacity = capacity
        self.status = status

    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity must be greater than 0")
        
        if value < self.booked_seats:
            raise ValueError("Capacity cannot be less than booked seats")
        
        self.__capacity = value

    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, value):
        if not isinstance(value, ShowStatus):
            raise InvalidStatusError("Status must be a valid ShowStatus")
        
        self.__status = value

    @property
    def booked_seats(self):
        return self.__booked_seats
    
    @booked_seats.setter
    def booked_seats(self, value):
        if value < 0:
            raise ValueError("Booked seats cannot be negative")
        
        if value > self.capacity:
            raise ValueError("Booked seats cannot exceed capacity")
        
        self.__booked_seats = value

    @property
    def remaining_seats(self):
        return self.capacity - self.booked_seats
    
    @property
    def is_full(self):
        return self.remaining_seats == 0
    
    def display_info(self):
        print(f"Title: {self.__title}")
        print(f"Capacity: {self.capacity}")
        print(f"Booked Seats: {self.booked_seats}")
        print(f"Remaining Seats: {self.remaining_seats}")
        print(f"Is Full: {self.is_full}")
        print(f"Status: {self.status.value}")

    def cancel_show(self):
        self.status = ShowStatus.CANCELLED

    def book_tickets(self, customer, quantity):
        if quantity <= 0:
            raise InvalidBookingError("Quantity must be greater than 0")
        
        if quantity > MAX_TICKETS_PER_BOOKING:
            raise InvalidBookingError(f"Quantity must not exceed {MAX_TICKETS_PER_BOOKING} tickets")
        
        if self.status == ShowStatus.CANCELLED:
            raise ShowCancelledError("Cannot book tickets for a cancelled show")
        
        if self.status == ShowStatus.SOLD_OUT:
            raise ShowSoldOutError("Cannot book tickets for a sold out show")

        if quantity > self.remaining_seats:
            raise InvalidBookingError("Cannot book more tickets than remaining seats")
        
        self.booked_seats = self.booked_seats + quantity

        if self.booked_seats == self.capacity:
            self.status = ShowStatus.SOLD_OUT

        print(f"{customer.name} booked {quantity} ticket(s) successfully!")