#search for a specific character in a string using a while loop and break statement.
input_string = "This is pycharm"
search_char = "p"
index = 0
found = False
while index < len(input_string):
    if input_string[index] == search_char:
        found = True
        break
    index += 1
if found:
    print(f"The character '{search_char}' was found at index {index}.")
else:
    print(f"The character '{search_char}' was not found in the string.")
