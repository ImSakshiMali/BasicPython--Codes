#print the elements of a list skipping the negative numbers using a while loop and continue statement.
list = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
index = 0
while index < len(list):
    element = list[index]
    if element < 0:
        index += 1
        continue
    print(element)
    index += 1