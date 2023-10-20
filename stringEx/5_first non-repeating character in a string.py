#Write a Python program to find the first non-repeating character in a string.
def first_non_repeating_char(input_string):
    char_count = {}
    for c in input_string:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    # Find the first non-repeating character
    for c in input_string:
        if char_count[c] == 1:
            return c
    return None
input_string = input("Enter a string: ")
result = first_non_repeating_char(input_string)

if result is not None:
    print("The first non-repeating character is:", result)
else:
    print("No non-repeating character found in the string.")
