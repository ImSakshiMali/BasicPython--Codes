#remove duplicate elements from a set.
set = set()
my_list = [1, 2, 3, 3, 4, 4, 5]  # A list with duplicates
for element in my_list:
    set.add(element)
print(set)
