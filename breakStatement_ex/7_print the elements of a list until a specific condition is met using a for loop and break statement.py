#print the elements of a list until a specific condition is met using a for loop and break statement.
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
stop= 9
for number in numbers:
    if number == stop:
        break
    print(number)
