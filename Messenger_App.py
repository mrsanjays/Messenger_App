from abc import ABC, abstractmethod
import re
class MessagingService(ABC):
    @abstractmethod
    def SendMessage(self):
        pass
class SMSMessagingService(MessagingService):
    def SendMessage(self,message,number):
        print(f"Message was Successfully sent to {number}")
class EmailMessagingService(MessagingService):
    def SendMessage(self, message, email):
        print(f"Message was Successfully sent to {email}")
class WhatsAppMessagingService(MessagingService):
    def SendMessage(self, message, number):
        print(f"Message was Successfully sent to {number}")

class Validate:
    def IsvalidNumber(self,num):
        Pattern=re.compile("^[6-9]\d{9}$")
        return Pattern.match(num)
    def IsvalidEMmail(self,email):
        Pattern = r'[^@]+@[^@]+\.[a-z]+'
        return re.match(Pattern, email)

if __name__ == '__main__':
    obj1= SMSMessagingService()
    obj2=EmailMessagingService()
    obj3=WhatsAppMessagingService()
    validate=Validate()
    while True:
        print("Enter 1 to Send SMS \nEnter 2 to Send Email \nEnter 3 to Send WhatsApp \nEnter 4 to quit")
        x=int(input("ENTER:"))
        if x == 4:
            print("Thank You!")
            quit()
        if x==1:
            number=input("Enter number:")
            if validate.IsvalidNumber(number):
                message=input("Enter Message to send :")
                obj1.SendMessage(message,number)
            else:
                print("Invalid Number")
        if x==2:
            email=input("Enter Email ID:")
            if validate.IsvalidEMmail(email):
                message=input("Enter the Message (Not more than 300 words) :")
                obj2.SendMessage(message,email)
            else:
                print("Incorrect mail Id")
        if x==3:
            number = input("Enter number:")
            if validate.IsvalidNumber(number):
                message = input("Enter Message to send :")
                obj3.SendMessage(message, number)
            else:
                print("Invalid Number")