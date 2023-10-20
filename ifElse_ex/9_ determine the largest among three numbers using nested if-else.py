# determine the largest among three numbers using nested if-else.
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
n3 = float(input("Enter the third number: "))
if n1 >= n2:
    if n1 >= n3:
        largest = n1
    else:
        largest = n3
else:
    if n2 >= n3:
        largest = n2
    else:
        largest = n3
print(f"The largest number among {n1}, {n2}, and {n3} is : {largest}.")
