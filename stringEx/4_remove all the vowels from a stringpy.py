#Write a Python program to remove all the vowels from a string.
def remove_vowels(i_s):  # input string i_s
    vowels = "AEIOUaeiou"
    result = ""
    for char in i_s:
        if char not in vowels:
            result += char
    return result
i_s = input("Enter a string: ")
o_s = remove_vowels(i_s) # output string o_s
print("String without vowels:", o_s)
