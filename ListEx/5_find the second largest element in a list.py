# Write a Python program to find the second largest element in a list.
def second_largest(list):
    temp = sorted(set(list))
    if len(temp) == 1:
        return -1
    return temp[-2]
list = list(map(int,input('Enter list as space separated numbers : ').strip().split()))
print('Second largest element in list is: ', second_largest(list))
