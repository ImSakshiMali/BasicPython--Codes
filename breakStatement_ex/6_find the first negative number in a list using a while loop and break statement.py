#find the first negative number in a list using a while loop and break statement.
index = 0
found = None
numbers = [1, 3, -5, 7, 9, -11, 13, 15, 17, 19]
while index < len(numbers):
    if numbers[index] < 0:
        found = numbers[index]
        break
    index += 1
if found is not None:
    print("The first negative number in the list is:",found)
else:
    print("No negative number was found in the list.")
