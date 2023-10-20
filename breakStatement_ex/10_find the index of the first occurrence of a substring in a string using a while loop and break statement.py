#find the index of the first occurrence of a substring in a string using a while loop and break statement.

str = "Hello, this is a sample string. This is a substring example."
substring = "is a"
first_occurrence_index = -1
index = 0
while index < len(str):
    if str[index:index + len(substring)] == substring:
        first_occurrence_index = index
        break
    index += 1
if first_occurrence_index != -1:
    print(f"The first occurrence of '{substring}' starts at index {first_occurrence_index}.")
else:
    print(f"'{substring}' was not found in the string.")
