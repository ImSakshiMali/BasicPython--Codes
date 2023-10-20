#sort a list of strings in alphabetical order.
input_string = input("Enter a list of strings separated by spaces: ")
input_list = input_string.split()
sorted_list = sorted(input_list)
print("Sorted list of strings:")
for string in sorted_list:
    print(string)
