#check if a character is a vowel or consonant.
char = input("Enter a character: ")
char = char.lower()
if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    print(f"{char} is a vowel.")
else:
    print(f"{char} is a consonant.")
