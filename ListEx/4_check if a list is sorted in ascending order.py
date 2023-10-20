#Write a Python program to check if a list is sorted in ascending order.
def sortasc(list):
    print(sorted(list))
    print(list)
    return list == sorted(list)
list = list(map(int,input('Enter list as space separated numbers : ').strip().split()))
print('whether list is sorted or not: ', sortasc(list))
