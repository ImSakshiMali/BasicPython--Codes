#iterate over a string and print only the consonants using a for loop and continue statement.
input_string = "Consonants"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
for char in input_string:
    if char not in consonants:
        continue
    print(char)
