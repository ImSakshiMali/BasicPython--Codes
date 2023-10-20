#search for a specific element in a list using a while loop and break statement.
def search_element(numbers, target):
    i = 0
    while i < len(numbers):
        if numbers[i] == target:
            print(f"{target} found at index {i}.")
            break
        i += 1
    else:
        print(f"{target} not found in the list.")
numbers = [10, 20, 30, 40, 50, 60]
target = 40
search_element(numbers, target)