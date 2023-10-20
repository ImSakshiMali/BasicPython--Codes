#print the squares of all numbers in a range.
def squares_in_range(start, end):
    for number in range(start, end + 1):
        square = number ** 2
        print(f"The square of {number} is {square}")
squares_in_range(1, 10)
