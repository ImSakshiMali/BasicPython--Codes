#find the common elements between two lists.
def common_ele(l1, l2):
    return list(set(l1) & set(l2))

l1 = [int(x) for x in input("Enter the first list of numbers separated by spaces: ").split()]
l2 = [int(x) for x in input("Enter the second list of numbers separated by spaces: ").split()]
common_ele_list = common_ele(l1, l2)
print("Common elements are :", common_ele_list)