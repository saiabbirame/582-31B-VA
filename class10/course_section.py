class CourseSection:
    def __init__(self, title, capacity, enrolled):
        if len(title.strip()) == 0:
            print("Title cannot be empty")
            return

        self.title = title

        self.__capacity = 1
        self.__enrolled = 0

        self.capacity = capacity
        self.enrolled = enrolled

    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, value):
        if value > 0:
            if self.__enrolled <= value:
                self.__capacity = value
            else:
                print("Capacity cannot be smaller than enrolled students")
        else:
            print("Capacity must be greater than 0")

    @property
    def enrolled(self):
        return self.__enrolled
    
    @enrolled.setter
    def enrolled(self, value):
        if value >= 0:
            if value <= self.__capacity:
                self.__enrolled = value
            else: 
                print("Enrolled students cannot exceed capacity")
        else:
            print("Enrolled students cannot be negative")

    def register_student(self):
        if self.enrolled < self.capacity:
            self.enrolled = self.enrolled + 1
        else:
            print("Course is full")

    def drop_student(self):
        if self.enrolled > 0:
            self.enrolled = self.enrolled - 1
        else:
            print("No students to drop")

    def display_info(self):
        print("Course Information:")
        print(f"Title: {self.title}")
        print(f"Capacity: {self.capacity}")
        print(f"Enrolled: {self.enrolled}")