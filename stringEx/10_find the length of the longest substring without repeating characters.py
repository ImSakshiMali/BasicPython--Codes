# Write a Python program to find the length of the longest substring without repeating characters.
# by user input
string = input("Enter the string:")
list = string.split(' ')
res = -1
res_word = ''
for word in list:
    if len(word) > res and len(word) == len(set(word)):
        res = len(word)
        res_word = word
print('Length of the longest substring without repeating characters: ', res,'- for word -->', res_word)
