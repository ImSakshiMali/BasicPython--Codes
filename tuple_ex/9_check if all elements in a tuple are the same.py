#check if all elements in a tuple are the same.
my_tuple = (2,2,2,2,2,2)
unique_elements_set = set(my_tuple)
if len(unique_elements_set) == 1:
    print("All elements in the tuple are the same.")
else:
    print("All elements in the tuple are not same.")
