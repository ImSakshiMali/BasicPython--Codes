#Write a python program to find the most frequent character in a string.
def most_frequent_character(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    most_frequent_char = max(char_count, key=char_count.get)

    return most_frequent_char
s = input("Enter a string:")
r = most_frequent_character(s)
print(f"The most frequent character is '{r}'")

