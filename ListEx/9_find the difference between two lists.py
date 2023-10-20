#find the difference between two lists.
def list_difference(l1, l2):
    return list(set(l1) - set(l2))

list1 = [int(x) for x in input("Enter the first list of numbers separated by spaces: ").split()]
list2 = [int(x) for x in input("Enter the second list of numbers separated by spaces: ").split()]
difference_list = list_difference(list1, list2)
print("Difference between lists:", difference_list)