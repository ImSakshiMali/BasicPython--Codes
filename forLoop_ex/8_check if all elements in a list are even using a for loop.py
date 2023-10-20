#check if all elements in a list are even using a for loop.
def are_all_even(lst):
    for num in lst:
        if num % 2 != 0:
            return False
    return True
my_list = [2, 4, 6, 8]
result = are_all_even(my_list)
if result:
    print("All elements are even.")
else:
    print("Not all elements are even.")
