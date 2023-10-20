#check if a number is present in a list using a while loop and break statement.
numbers = [10, 20, 30, 40, 50, 60, 70]
target = 30
number_found = False
index = 0
while index < len(numbers):
    if numbers[index] == target:
        number_found = True
        break
    index += 1
if number_found:
    print(f"{target} is present in the list.")
else:
    print(f"{target} is not present in the list.")
