# find the largest element in a list using a for loop.
numbers = [3, 1, 7, 4, 9, 2]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest element:", largest)