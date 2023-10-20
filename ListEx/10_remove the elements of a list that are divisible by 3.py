#remove the elements of a list that are divisible by 3.
def remove_divisible_by_3(lst):
    return [x for x in lst if x % 3 != 0]

list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
result = remove_divisible_by_3(list)
print("List without elements divisible by 3 :", result)