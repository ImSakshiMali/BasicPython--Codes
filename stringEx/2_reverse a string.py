#Write a Python program to reverse a string.
def rev_string(s):
    return s[::-1]
input_string = input("Enter a string: ")
reversed_str = rev_string(input_string)
print("Reversed string:", reversed_str)