#check if a set is a subset of another set.
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
is_subset = set1.issubset(set2)
if is_subset:
    print("set1 is a subset of set2")
else:
    print("set1 is not a subset of set2")
