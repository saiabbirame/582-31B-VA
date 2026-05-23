class StudentRecord:
    def __init__(self, name, gpa, credits):
        if len(name.strip()) == 0:
            print("Name cannot be empty")
            return

        self.name = name

        self.__gpa = 0.0
        self.__credits = 0

        self.gpa = gpa
        self.credits = credits

    @property 
    def gpa(self):
        return self.__gpa
    
    @gpa.setter
    def gpa(self, value):
        if value >= 0.0 and value <= 4.0:
            self.__gpa = value
        else:
            print("Invalid GPA")

    @property 
    def credits(self):
        return self.__credits
    
    @credits.setter
    def credits(self, value):
        if value >= 0:
            self.__credits = value
        else:
            print("Credits cannot be negative")

    @property
    def academic_status(self):
        if self.gpa >= 3.5:
            return "Honours"
        elif self.gpa >= 2.0:
            return "Good Standing"
        else:
            return "At Risk"

    def add_credits(self, amount):
        if amount >= 0:
            self.credits = self.credits + amount
        else:
            print("Cannot add negative credits")

    def update_gpa(self, value):
        self.gpa = value

    def display_info(self):
        print("Student Information:")
        print(f"Name: {self.name}")
        print(f"GPA: {self.gpa}")
        print(f"Credits: {self.credits}")