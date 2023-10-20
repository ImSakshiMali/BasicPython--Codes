#Write a Python program to remove duplicates from a list.
def removedup(list):
    res = []
    for element in list:
        if element not in res:
            res.append(element)
        else:
            continue
    return res
list = list(map(int,input('Enter list with  numbers separated by space : ').strip().split()))
print('List after removing duplicates: ',removedup(list))
