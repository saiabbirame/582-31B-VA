from course import Course
from status import CourseStatus, DeliveryMode

course1 = Course("Advanced Programming", 30, CourseStatus.OPEN, DeliveryMode.IN_PERSON)
course2 = Course("Web Interface Programming 2", 25, CourseStatus.CLOSED, DeliveryMode.ONLINE)

course1.display_info()
course2.display_info()

course1.close_registration()
course1.display_info()

course2.reopen_course()
course2.display_info()

print(course1.is_open_for_registration())
print(course2.is_open_for_registration())