# find the first occurrence of a vowel in a string using a for loop and break statement.
def find_first_vowel(text):
    for index, char in enumerate(text):
        if char.lower() in 'aeiou':
            print(f"The first vowel '{char}' is at index {index}")
            break
    else:
        print("No vowels found in the string")

text = "This is pycharm."
find_first_vowel(text)