#print the elements of a list skipping the elements divisible by 3 using a for loop and continue statement.
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for element in list:
    if element % 3 == 0:
        continue
    print(element)
