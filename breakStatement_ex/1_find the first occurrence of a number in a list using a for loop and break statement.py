#find the first occurrence of a number in a list using a for loop and break statement.
numbers = [10, 20, 30, 40, 50, 60, 70]
target = 40
first_occurrence_index = None
for index, number in enumerate(numbers):
    if number == target:
        first_occurrence_index = index
        break
if first_occurrence_index is not None:
    print(f"The first occurrence of {target} is at index {first_occurrence_index}.")
else:
    print(f"{target} was not found in the list.")

