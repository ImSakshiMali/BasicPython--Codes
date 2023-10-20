#find the common elements between two lists using a while loop.
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_elements = []
index1 = 0
while index1 < len(list1):
    index2 = 0
    while index2 < len(list2):
        if list1[index1] == list2[index2]:
            common_elements.append(list1[index1])
            break
        index2 += 1
    index1 += 1
print("Common elements:", common_elements)