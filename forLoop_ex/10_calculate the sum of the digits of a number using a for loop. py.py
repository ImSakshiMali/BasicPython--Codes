#calculate the sum of the digits of a number using a for loop.

num = input("Enter a number: ")
sum = 0
for digit in num:
    sum += int(digit)
print("Sum of the digits:", sum)
