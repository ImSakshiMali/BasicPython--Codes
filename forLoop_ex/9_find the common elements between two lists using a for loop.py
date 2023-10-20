#find the common elements between two lists using a for loop.
l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5, 6, 7]
common_elements = []
for item1 in l1:
    if item1 in l2:
        common_elements.append(item1)
print("Common elements:", common_elements)
