#Write a Python program to check if a string is a valid email address.
import re

def is_valid_email(email):
    if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$",email):
         return True
    return False

email = input("Enter an email address: ")
if is_valid_email(email):
    print("Valid email address")
else:
    print("Invalid email address")
