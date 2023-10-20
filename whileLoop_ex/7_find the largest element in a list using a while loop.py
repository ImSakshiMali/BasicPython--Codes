#find the largest element in a list using a while loop.
list = [1,2,5,8,4,99,3,101]
x = 0
index = 0
while index != len(list):
    if x < list[index]:
        x = list[index]
    index += 1
print ("Largest element in list :",x)