#Write a Python program to check if a string is a palindrome.
def is_palindrome(string):
    return string == string[::-1]

input_string = input("Enter a string: ")
result = is_palindrome(input_string)
print("Palindrome status :", result)