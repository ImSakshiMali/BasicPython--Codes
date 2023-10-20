#check if all elements in a list are even using a while loop.
list = [2, 4, 6, 8, 10]
i = 0
all_even = True
while i < len(list):
    if list[i] % 2 != 0:
        all_even = False
        break
    i += 1
if all_even:
    print("All elements are even.")
else:
    print("Not all elements are even.")