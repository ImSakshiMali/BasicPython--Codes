#check if two sets are disjoint.

s1 = {1, 2, 3}
s2 = {4, 5, 6}
disjoint = s1.isdisjoint(s2)
print(s1.isdisjoint(s2))
if disjoint:
    print("The sets are disjoint.")
else:
    print("The sets are not disjoint.")