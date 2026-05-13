# implement a basic notification system

# 1. I want an interface / abstract class of Notification
# abstractmethod --> send(self, message)

#2. two concrete implementations of this class

#EmailNotification class
#SMSNotification class

#3. then use them here

from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def __init__(self, email):
        self.email = email

    def send(self, message):
        print(f"Email to: {self.email}")
        print(f"Message: {message}")

class SMSNotification(Notification):
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def send(self, message):
        print(f"SMS to: {self.phone_number}")
        print(f"Message: {message}")

def notify(notification, message):
    notification.send(message)

email_user = EmailNotification("abc@gmail.com")
sms_user = SMSNotification("123-456-7890")

notify(email_user, "Hey!")

notify(sms_user, "Hello!")