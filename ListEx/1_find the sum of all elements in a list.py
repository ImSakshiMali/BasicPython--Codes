#Write a python program to find the sum of all elements in a list.
def sum_of_list_elements(lst):
    total = 0
    for element in lst:
        total += element
    return total
list = [1,2,3,4]
result = sum_of_list_elements(list)
print("Sum of elements in the list:", result)
