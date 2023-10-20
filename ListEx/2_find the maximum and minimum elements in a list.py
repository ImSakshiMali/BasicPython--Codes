#find the maximum and minimum elements in a list.
def max_min_elements(lst):
    if not lst:
        return None, None
    return max(lst), min(lst)
list = [int(x) for x in input("Enter a list of no. separated by spaces: ").split()]
max_val, min_val = max_min_elements(list)
print("Maximum element:", max_val)
print("Minimum element:", min_val)