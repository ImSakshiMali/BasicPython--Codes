#print the cube of all numbers in a range.
def cubes_in_range(start, end):
    for number in range(start, end + 1):
       cube = number**4
       print(f"The cube of {number} is {cube}")
cubes_in_range(1,10)
