from student_record import StudentRecord
from course_section import CourseSection

print("Valid Student Tests:")

student1 = StudentRecord("Jane Doe", 3.2, 33)

student1.display_info()
print()

student1.add_credits(6)
student1.update_gpa(3.6)
student1.display_info()
print()

print("Invalid Student Tests:")

student1.update_gpa(4.8)
student1.add_credits(-6)
print()

student2 = StudentRecord("", 2.8, 6)
print()

print("Valid Course Tests:")

course1 = CourseSection("Dynamic Web Programming", 3, 0)

course1.display_info()
print()

course1.register_student()
course1.register_student()
course1.register_student()
course1.display_info()
print()

print("Invalid Course Tests:")

course1.register_student()
print()

course1.drop_student()
course1.drop_student()
course1.drop_student()
course1.drop_student()
print()

course2 = CourseSection("", 9, 0)
course3 = CourseSection("Web Interface Programming 1", 0, 0)
print()