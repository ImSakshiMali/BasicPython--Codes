#print the uppercase letters in a string using a while loop and continue statement.
input_string = "UpperCase"
index = 0
while index < len(input_string):
    char = input_string[index]
    if not char.isupper():
        index += 1
        continue
    print(char)
    index += 1

